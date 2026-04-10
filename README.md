# SQL and NoSQL Flask web server

**CS178: Cloud and Database Systems — Project #1**
**Author:** Bernardo
**GitHub:** CallingBoar

---

## Overview

Creates a website with multiple routes that connects to an RDS SQL database holding movies and movie information, and a Dynamo NoSQL database with countries and country information. There is full CRUD functionality for the NoSQL database. Custom queries can be used on the SQL database.

---

## Technologies Used

- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for movies and movie information
- **AWS DynamoDB** — non-relational database for countries and the popeulation density of countries (popes per square mile)

---

## Project Structure

```
ProjectOne/
├── flaskapp.py              # Main Flask application — routes and app logic
├── dbCode.py                # Database helper functions (MySQL connection + queries)
├── creds.py                 # Sample credentials file (see Credential Setup below)
├── add_country_file.py      # Helper function with functions to add data to the DynamoDB table
├── delete_country_file.py   # Helper function with functions to remove data from the DynamoDB table
├── read_countries_file.py   # Helper function with functions to return data from the DynamoDB table
├── add_country_file.py      # Helper function with functions to update dat in the DynamoDB table
├── templates/
│   ├── home.html                     # Landing page
│   ├── add_country.html              # asks user for info on adding a country
│   ├── delete_country.html           # asks user for the name of the country to be deleted
│   ├── display_country.html          # displays all countries in a table
│   ├── update_country.html           # asks user for info to update a country
│   ├── query_movies.html             # asks user for query for SQL database, with diagram
│   ├── query_movies_exception.html   # displays if a user inputs a query that fails for whatever reason
├── static/
│   ├── movies_diagram.jpg   # displays in query_movies page
├── .gitignore               # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/CallingBoar/cs178-flask-app
   cd cs178-flask-app
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://127.0.0.1:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
http://ec2-44-193-198-248.compute-1.amazonaws.com:8080/
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "your-rds-endpoint"
user = "admin"
password = "your-password"
db = "your-database-name"
```

---

## Database Design

### SQL (MySQL on RDS)

<!-- Briefly describe your relational database schema. What tables do you have? What are the key relationships? -->

**Example:**

- `movie` — stores movie titles and basic information; primary key is `movie_id`
- `production_country` — stores connections between movies and countries of production; primary key is `movie_id, country_id`; foreign keys link to `movie` and `country`
- `country` — stores country information; primary key is `country_id`; foreign key links to `production_country`
- `movie_languages` — stores connections between movies and langages; primary key is `movie_id, language_id, language_role_id`; foreign keys link to `movie`, `language`, and `language_role`
- `language` — stores different languages; primary key is `language_id`; foreign key links to `movie_languages`
- `language_role` — stores whether a movie is spoken or original; primary key is `role_id`; foreign key links to `movie_languages`
- `movie_genre` — stores connections between movies and genres; primary key is `movie_id, genre_id`; foreign keys link to `movie` and `genre`
- `genre` — stores different genres and their id's; primary key is `genre_id`; foreign key links to `movie_genre`
- `movie_keywords` — stores connections for movie and keywords; primary key is `movie_id, keyword_id`; foreign keys link to `movie` and `keyword`
- `keyword` — stores different keywords that can relate to movies; primary key is `keyword_id`; foreign key links to `movie_keywords`
- `movie_company` — stores connections for movie and production_company; primary key is `movie_id, company_id`; foreign keys link to `movie` and `production_company`
- `production_company` — stores names of companies that make movies; primary key is `company_id`; foreign key links to `movie_company`
- `movie_cast` — stores connections between movies, actors and actresses, as well as a table for gender; primary key is `movie_id, gender_id, person_id`; foreign key links to `movie`, `gender`, and `person`
- `gender` — stores gender of different people; primary key is `gender_id`; foreign key links to `movie_cast`
- `person` — stores names of people; primary key is `person_id`; foreign key links to `movie cast` and `movie_crew`
- `movie_crew` — stores info on people, what department the work for, and for what movie; primary key is `person_id, movie_id, department_id`; foreign key links to `movie`, `person`, and `department`
- `department` — stores info on departments; primary key is `department_id`; foreign key links to `movie_crew`

The JOIN query used in this project: outputs the movie_id, movie_title, and genre for every movie

### DynamoDB

<!-- Describe your DynamoDB table. What is the partition key? What attributes does each item have? How does it connect to the rest of the app? -->

- **Table name:** `Countries`
- **Partition key:** `Name`
- **Used for:** Holding country names and popeulation densities

---

## CRUD Operations

| Operation | Route              | Description                        |
| --------- | ------------------ | ---------------------------------- |
| Create    | `/add-country`     | Allows user to add new countries   |
| Read      | `/display-country` | Displays all countries to the user |
| Update    | `/update-country`  | Allows user to update countries    |
| Delete    | `/delete-country`  | Allows user to delete countries]   |

---

## Challenges and Insights

The hardest part of the creation of this was the connecting of all the different services together. This project involves connecting data and instructions to and from both databases, SQL and No SQL, Python, Flask, HTML, and finally the user, who could be anywhere in the world. I was able to allow the user to input any SQL query they wanted, allowing for tons of versatility.

---

## AI Assistance

ChatGPT was used in the creation of update_countries_file.py. It was used as the update function had some weird syntax I had trouble with. It also helped me understand how to use images in flask, as I had forgotten that the image must be in a folder named static.
