# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *
import creds
# import cryptography

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
        continent = request.form['continent']
        
        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        print("Name:", name, ":", "Continent:", continent)
        
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
        
        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        print("Name to delete:", name)
        
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
        continent = request.form['continent']


        print("Country to update:", name, "Value to replace continent:", continent)


        flash('Country deleted successfully! Hoorah!', 'warning')
        return redirect(url_for('home'))
    else:
        return render_template('update_country.html')

@app.route('/display-users')
def display_users():
    # hard code a value to the users_list;
    # note that this could have been a result from an SQL query :) 
    rows = execute_query("""
        SELECT *
        FROM country;
    """)

    # users_list = (('John','Doe','Comedy'),('Jane', 'Doe','Drama'))
    # return render_template('display_users.html', users = users_list)
    return display_html(rows)


# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
