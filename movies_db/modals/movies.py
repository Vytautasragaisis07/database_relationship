from database import insert_query, get_database, create_table_database
from entities.movie import movie


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies (
                        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name TEXT UNIQUE,
                        release_date TEXT,
                        rating TEXT,
                        box_office_name TEXT,
                        studio_name TEXT)"""

    create_table_database(query)


create_movies_table()

#get_database('PRAGMA table_info(movies)')
#create_table_database('DROP TABLE movies')

movie1 = movie(None, "Harry Potter", "2017", "9.8", "Director", "Studio", "Studio_name")

def create_movie(movie):
    query = "INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?)"
    params = (movie.movie_id, movie.movie_name, movie.release_date, movie.rating, movie.box_office_name, movie.studio_name)
    database.get_database(query, params)

def get_movie(movie):
    query = "SELECT * FROM movies WHERE movie_id = (?) OR movie_name = (?) OR release_date = (?) OR  rating = (?) OR box_office_name = (?) OR studio_name = (?)"
    params = (movie.movie_id, movie.movie_name, movie.release_date, movie.rating, movie.box_office_name, movie.studio_name)
    database.insert_query(query, params)

#create_movie(movie1)

#get_movie(movie1)



