from database.database import create_table_database, insert_query, get_database
from entities.movie import movie


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies(
                        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name TEXT UNIQUE,
                        release_date DATE,
                        rating REAL,
                        genre TEXT
                        )"""
    create_table_database(query)


create_movies_table()

# get_database('PRAGMA table_info(movies)')
# create_table_database('DROP TABLE movies')


movie1 = movie(None, "Harry Potter", 2001, 7, "Magic")

def create_movie(movie):
    query = "INSERT INTO movies VALUES (?, ?, ?, ?, ?)"
    params = (movie.movie_id, movie.movie_name, movie.release_date, movie.rating, movie.genre)
    insert_query(query, params)

def get_movie(movie):
    query = "SELECT * FROM movies WHERE movie_id = (?) OR movie_name = (?) OR release_date = (?) OR rating = " \
                "(?) OR genre = (?)"

    params = (movie.movie_id, movie.movie_name, movie.release_date, movie.rating, movie.genre)
    get_database(query, params)


def update_movie(movie):
    query = "UPDATE movies SET movie_name = 'Harry Potter' WHERE movie_name = (?)"
    params = (movie.movie_name,)
    insert_query(query, params)


def delete_movie(movie):
    query = "DELETE FROM movies WHERE movie_id = (?) OR movie_name = (?) OR release_date = (?) OR rating = " \
            "(?) OR genre = (?)"
    params = (movie.movie_id, movie.movie_name, movie.release_date, movie.rating, movie.genre)
    insert_query(query, params)

# delete_movie(movie1)
# update_movie(movie1)
# get_movie(movie1)
# create_movie(movie1)
