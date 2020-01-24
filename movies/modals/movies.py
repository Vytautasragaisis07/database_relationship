from movies.database import create_table_database


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movie (
                        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name
                        release_date
                        rating
                        box_office_name
                        studio_name TEXT)"""
    create_table_database(query)


create_movies_table()
