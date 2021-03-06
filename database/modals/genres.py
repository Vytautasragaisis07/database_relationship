from database.database import create_table_database, insert_query, get_database
from entities.genre import genre


def create_genres_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


def create_movies_genres_table():
    query = """CREATE TABLE IF NOT EXISTS movie_genres (
                        genre_movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        genre_id int,
                        movie_id int,
                        genre_id FOREIGN KEY (genre_id) REFERENCES actors(genre_id),
                        movie_id FOREIGN KEY (movie_id) REFERENCES actors(movie_id)"""
    create_table_database(query)


create_genres_table()

# create_movies_genres_table()
# create_table_database('DROP TABLE genres')
# get_database('PRAGMA table_info(genres)')

genre1 = genre(None, "Criminal")

def create_genre(genre):
    query = "INSERT INTO genres VALUES (?, ?)"
    params = (genre.genre_id, genre.name)
    insert_query(query, params)

def get_genre(genre):
    query = "SELECT * FROM genres WHERE genre_id = (?) OR name = (?)"
    params = (genre.genre_id, genre.name)
    get_database(query, params)


def update_genre(genre):
    query = "UPDATE genres SET name = 'Criminal' WHERE name = (?)"
    params = (genre.name)
    insert_query(query, params)

def delete_genre(genre):
    query = "DELETE FROM genres WHERE genre_id = (?) OR name = (?)"
    params = (genre.genre_id, genre.name)
    insert_query(query, params)


create_genre(genre1)
get_genre(genre1)
update_genre(genre1)
delete_genre(genre1)

