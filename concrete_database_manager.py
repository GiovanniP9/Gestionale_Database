import mysql.connector
from mysql.connector import Error
from abstract_database_manager import DatabaseManagerBase


# Decoratore per gestire l'apertura e chiusura del cursore e il commit automatico
def auto_commit(method):
    def wrapper(self, *args, **kwargs):
        cursor = self.connection.cursor()
        try:
            result = method(self, cursor, *args, **kwargs)
            self.connection.commit()  # conferma le modifiche
            return result
        except Error as e:
            print(f"Errore: {e}")
        finally:
            cursor.close()
    return wrapper


class MySQLDatabaseManager(DatabaseManagerBase):
    # Costruttore: inizializza parametri di connessione
    def __init__(self, host="localhost", user="root", password=""):
        self.host = host
        self.user = user
        self.password = password


    # Connessione al server MySQL
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Connessione al server MySQL riuscita.")
        except Error as e:
            print(f"Errore durante la connessione: {e}")

    # Creazione database (decorato per gestire commit e cursore)
    @auto_commit
    def create_database(self, cursor, name):
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
        print(f"Database '{name}' creato.")

    # Connessione al database specifico; se non esiste lo crea
    def connect_to_database(self, name):
        try:
            self.connection.database = name
            print(f"Connesso al database '{name}'.")
        except Error:
            print(f"Database '{name}' non trovato. Tentativo di creazione...")
            self.create_database(name)
            self.connection.database = name

    # Crea una nuova tabella
    @auto_commit
    def create_table(self, cursor):
        table_name = input("Nome tabella: ")
        columns = input("Definizione colonne (es. id INT, nome VARCHAR(100)): ")
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        cursor.execute(query)
        print(f"Tabella '{table_name}' creata.")

    # Aggiunge una colonna a una tabella
    @auto_commit
    def add_column(self, cursor):
        table = input("Nome tabella: ")
        col_def = input("Definizione colonna (es. eta INT): ")
        query = f"ALTER TABLE {table} ADD COLUMN {col_def}"
        cursor.execute(query)
        print("Colonna aggiunta.")

    # Elimina una colonna da una tabella
    @auto_commit
    def delete_column(self, cursor):
        table = input("Nome tabella: ")
        col = input("Nome colonna da eliminare: ")
        query = f"ALTER TABLE {table} DROP COLUMN {col}"
        cursor.execute(query)
        print("Colonna eliminata.")

    # Elimina una tabella
    @auto_commit
    def delete_table(self, cursor):
        table = input("Nome tabella: ")
        query = f"DROP TABLE IF EXISTS {table}"
        cursor.execute(query)
        print("Tabella eliminata.")

    # Inserisce dati nella tabella
    @auto_commit
    def insert_data(self, cursor):
        table = input("Nome tabella: ")
        cols = input("Colonne (es. nome, eta): ")
        vals = input("Valori (es. 'Mario', 25): ")
        query = f"INSERT INTO {table} ({cols}) VALUES ({vals})"
        cursor.execute(query)
        print("Dati inseriti.")

    # Aggiorna dati nella tabella
    @auto_commit
    def update_data(self, cursor):
        table = input("Nome tabella: ")
        set_clause = input("SET (es. nome='Luca'): ")
        where_clause = input("WHERE (es. id=1): ")
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        cursor.execute(query)
        print("Dati aggiornati.")

