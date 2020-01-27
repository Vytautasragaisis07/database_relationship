from movies.database import create_table_database


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        director_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        director_name TEXT)"""
    create_table_database(query)


create_actors_table()
