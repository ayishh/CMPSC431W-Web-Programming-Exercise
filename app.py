from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


@app.route('/')
def index():
    return render_template('index.html')

# Add a new patient
@app.route('/addPatient', methods=['POST', 'GET'])
def addPatient():
    error = None

    # Create a connection to the database
    connection = sql.connect('database.db')

    # Create a table named users if it does not exist, with columns pid (primary key), firstname, and lastname
    connection.execute('CREATE TABLE IF NOT EXISTS users(pid INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT);')

    # If the request method is POST, insert the first name and last name into the database
    if request.method == 'POST':
        # Insert the patient with the given first name and last name into the database
        connection.execute('INSERT INTO users (firstname, lastname) VALUES (?,?);', (request.form['FirstName'], request.form['LastName']))
        connection.commit()

    # If the request method is GET, we want to show the list of patients in the database OR After adding a patient, we want to show the updated list of patients in the database
    cursor = connection.execute('SELECT * FROM users;')
    result = cursor.fetchall()

    # Render the addPatient.html 
    return render_template('addPatient.html', error=error, result=result)

# Delete a patient
@app.route('/deletePatient', methods=['POST', 'GET'])
def deletePatient():
    error = None

    # Create a connection to the database
    connection = sql.connect('database.db')

    connection.execute('CREATE TABLE IF NOT EXISTS users(pid INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT);')

    if request.method == 'POST':
        
        # Delete the patient with the given first name and last name from the database
        connection.execute('DELETE FROM users WHERE firstname=? AND lastname=?;', (request.form['FirstName'], request.form['LastName']))
        connection.commit()

    # After deleting the patient, we want to show the updated list of patients
    cursor = connection.execute('SELECT * FROM users;')
    result = cursor.fetchall()

    return render_template('deletePatient.html', result=result, error=error)

if __name__ == "__main__":
    app.run()


