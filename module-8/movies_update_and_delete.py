import mysql.connector
from mysql.connector import errorcode

def show_films(cursor, title):
    print("\n-- " + title + " --\n" + "=" * (len(title) + 6))
    query = """
    SELECT film.film_name, film.film_director, genre.genre_name, studio.studio_name 
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    films = cursor.fetchall()
    
    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name ID: {film[2]}\nStudio Name: {film[3]}\n")

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Carrots2025#",
        database="movies"
    )
    cursor = db.cursor()

    # Display current films
    show_films(cursor, "DISPLAYING FILMS")
    
    # Insert a new film (ensure studio_id and genre_id exist)
    insert_query = """
    INSERT INTO film (film_name, film_releaseDate, film_director, genre_id, studio_id)
    VALUES ('Interstellar', 2014, 'Christopher Nolan', 1, 2)
    """  # Replace '1' and '2' with valid genre_id and studio_id from your DB
    cursor.execute(insert_query)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update Alien to Horror
    update_query = "UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien'"
    cursor.execute(update_query)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete Gladiator
    delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
    cursor.execute(delete_query)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    cursor.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist")
    else:
        print(err)


