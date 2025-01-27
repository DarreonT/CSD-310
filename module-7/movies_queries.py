# Import required libraries
import mysql.connector
from dotenv import dotenv_values

# Load the configuration from .env file
secrets = dotenv_values(".env")

# Database connection configuration
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

# Try to connect to the database
try:
    # Connect to the database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()  # Create a cursor object to interact with the database
    
    # Query 1: Select all fields from the studio table
    print("1. All fields from the studio table:")
    query1 = "SELECT * FROM studio;"
    cursor.execute(query1)
    studio_results = cursor.fetchall()  # Fetch all the results
    for row in studio_results:
        print(row)

    print("\n" + "-"*50 + "\n")  # Just a separator for better output formatting

    # Query 2: Select all fields from the genre table
    print("2. All fields from the genre table:")
    query2 = "SELECT * FROM genre;"
    cursor.execute(query2)
    genre_results = cursor.fetchall()
    for row in genre_results:
        print(row)

    print("\n" + "-"*50 + "\n")  # Separator

    # Query 3: Select movie names with a runtime of less than 2 hours
    print("3. Movies with a runtime of less than 2 hours:")
    query3 = "SELECT movie_name FROM movies WHERE run_time < 120;"
    cursor.execute(query3)
    short_movies = cursor.fetchall()
    for row in short_movies:
        print(row)

    print("\n" + "-"*50 + "\n")  # Separator

    # Query 4: Get a list of film names and directors grouped by director
    print("4. List of films and directors grouped by director:")
    query4 = "SELECT movie_name, director FROM movies GROUP BY director;"
    cursor.execute(query4)
    director_results = cursor.fetchall()
    for row in director_results:
        print(row)

except mysql.connector.Error as err:
    # Handle any errors that occur during the connection or query execution
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("The username or password is incorrect.")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("The database does not exist.")
    else:
        print(err)

finally:
    # Close the connection to the database when done
    if db.is_connected():
        cursor.close()
        db.close()
        print("\nConnection to the database closed.")
