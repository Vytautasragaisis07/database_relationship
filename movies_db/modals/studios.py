from database import create_table_database


def create_studios_table():
    query = """CREATE TABLE IF NOT EXISTS studios (
                        studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        studio_name TEXT)"""
    create_table_database(query)


create_studios_table()