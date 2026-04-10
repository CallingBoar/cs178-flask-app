# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *
import creds
# import functions from other .py files
import read_countries
import add_country_file
import delete_country_file
import update_country_file

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

def display_html(rows):
    """
    Converts query result rows into a simple HTML table string.
    Flask routes can return this directly as a response.
    """
    html = "<table border='1'>" + "<tr>"
    for colnames in rows[0]:
        html += f"<td>{colnames}</td>"
    for row in rows:
        html += "<tr>"
        for col in row:
            html += f"<td>{row[col]}</td>"
        html += "</tr>"
    html += "</table>"
    return html

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-country', methods=['GET', 'POST'])
def add_country():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        popeulation_density = request.form['popeulation_density']
        
        # Process the data (e.g., add it to a database)
        # use add country file to add add item
        add_country_file.add_country_to_dynamo({
            "Name": name,
            "Popeulation Density": popeulation_density
            })
        
        flash('Country added successfully! Huzzah!', 'success')  # 'success' is a category; makes a green banner at the top
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_country.html')

@app.route('/delete-country',methods=['GET', 'POST'])
def delete_country():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']

        # use delete country file to delete item
        delete_country_file.delete_country_from_dynamo(name)
        
        flash('Country deleted successfully! Hoorah!', 'warning')
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('delete_country.html')

@app.route('/update-country', methods=['GET', 'POST'])
def update_country():
    if request.method == 'POST':
        name = request.form['name']
        popeulation_density = request.form['popeulation_density']

        update_country_file.update_country_in_dynamo(name,popeulation_density)


        flash('Country updated successfully! Hoorah!', 'warning')
        return redirect(url_for('home'))
    else:
        return render_template('update_country.html')

@app.route('/display-countries')
def display_countries():

    return read_countries.countries_html()

@app.route('/display-movies')
def display_movies():
    # execute a query to get info for rows
    rows = execute_query("""
        SELECT movie.movie_id, movie.title, genre.genre_name
        FROM movie JOIN movie_genres JOIN genre
        WHERE movie.movie_id=movie_genres.movie_id AND movie_genres.genre_id=genre.genre_id
        ORDER BY title;
    """)

    # users_list = (('John','Doe','Comedy'),('Jane', 'Doe','Drama'))
    # return render_template('display_users.html', users = users_list)
    return display_html(rows)

@app.route('/query-movies', methods=['GET', 'POST'])
def query_movies():
    # allows users to submit their own queries
    if request.method == 'POST':
        try:
            query = request.form['query']
            rows = execute_query(query)
            return display_html(rows)
        except:
            return render_template('query_movies_exception.html')
    else:
        return render_template('query_movies.html')

# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
