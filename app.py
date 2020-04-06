# Isaac Krementsov
# 3/30/2020
# Introduction to Systems Engineering
# Flask DB Access - Select records from MariaDB

from flask import *
import mysql.connector
import json


# Initialize Flask app
app = Flask(__name__)


# Read MySQL connection credentials
credentials = json.load(open("credentials.json", "r"))

# Method to show database records
@app.route('/temp', methods=['GET'])
def temp():
    # Connect to MariaDB to access records
    database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )
    cursor = database.cursor()

    # Return records with ID 20 through 30 [inclusive]
    # from the test_data table
    query = "SELECT * FROM temperature_data;"

    # Execute the query and get the resultant data
    cursor.execute(query)
    data = cursor.fetchall()

    # Close the database session
    cursor.close()
    database.close()

    # Render the database records in an HTML page
    return render_template("temp_chart.html", data = data, name = 'Isaac Krementsov')


# Redirect users seeking '/' url to '/temp'
@app.route('/', methods=['GET'])
def default():
    return redirect(url_for('temp'))
