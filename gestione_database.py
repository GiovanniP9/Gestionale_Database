import mysql.connector
from mysql.connector import Error

# Funzione per connettersi al server MySQL
def connect_to_mysql_server():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='GiFeTe251098?'
        )
        if connection.is_connected():
            print("Connesso al server MySQL con successo.")
            return connection
        else:
            print("Impossibile connettersi al server MySQL.")
            return None
    except Error as e:
        print(f"Errore durante la connessione al server: {e}")
        return None

def conn_to_database(connection, database_name):
    try:
        connection.database = database_name
        print(f"Connesso al database {database_name} con successo.")
    except Error as e:
        print(f"Database '{database_name}' non trovato. Tentativo di creazione...")
        create_database(connection, database_name)
        try:
            connection.database = database_name
            print(f"Connesso al database {database_name} dopo la creazione.")
        except Error as e:
            print(f"Errore durante la connessione al database {database_name} dopo la creazione: {e}")

def create_database(connection, database_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"Database {database_name} creato con successo.")
    except Error as e:
        print(f"Errore durante la creazione del database {database_name}: {e}")
    finally:
        cursor.close()

def create_table(connection):
    table_name = input("Inserisci il nome della tabella: ")
    columns = input("Inserisci le colonne (es. id INT PRIMARY KEY, nome VARCHAR(100)): ")
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f"Tabella {table_name} creata con successo.")
    except Error as e:
        print(f"Errore durante la creazione della tabella {table_name}: {e}")
    finally:
        cursor.close()

def add_column(connection):
    table_name = input("Inserisci il nome della tabella a cui aggiungere la colonna: ")
    column_definition = input("Inserisci la definizione della colonna (es. nuova_colonna VARCHAR(100)): ")
    query = f"ALTER TABLE {table_name} ADD COLUMN {column_definition}"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f"Colonna aggiunta alla tabella {table_name} con successo.")
    except Error as e:
        print(f"Errore durante l'aggiunta della colonna alla tabella {table_name}: {e}")
    finally:
        cursor.close()

def delete_column(connection):
    table_name = input("Inserisci il nome della tabella da cui eliminare la colonna: ")
    column_name = input("Inserisci il nome della colonna da eliminare: ")
    query = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f"Colonna {column_name} eliminata dalla tabella {table_name} con successo.")
    except Error as e:
        print(f"Errore durante l'eliminazione della colonna {column_name} dalla tabella {table_name}: {e}")
    finally:
        cursor.close()

def delete_table(connection):
    table_name = input("Inserisci il nome della tabella da eliminare: ")
    query = f"DROP TABLE IF EXISTS {table_name}"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f"Tabella {table_name} eliminata con successo.")
    except Error as e:
        print(f"Errore durante l'eliminazione della tabella {table_name}: {e}")
    finally:
        cursor.close()

def insert_data(connection):
    table_name = input("Inserisci il nome della tabella in cui inserire i dati: ")
    columns = input("Inserisci le colonne (es. colonna1, colonna2): ")
    values = input("Inserisci i valori (es. 'valore1', 'valore2'): ")
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Dati inseriti nella tabella {table_name} con successo.")
    except Error as e:
        print(f"Errore durante l'inserimento dei dati nella tabella {table_name}: {e}")
    finally:
        cursor.close()

def update_data(connection):
    table_name = input("Inserisci il nome della tabella in cui aggiornare i dati: ")
    set_clause = input("Inserisci la clausola SET (es. colonna1='nuovo_valore'): ")
    where_clause = input("Inserisci la clausola WHERE (es. colonna2='valore'): ")
    query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Dati aggiornati nella tabella {table_name} con successo.")
    except Error as e:
        print(f"Errore durante l'aggiornamento dei dati nella tabella {table_name}: {e}")
    finally:
        cursor.close()

def manage_tables(connection):
    while True:
        print("\nGestione Tabelle:")
        print("1. Crea Tabella")
        print("2. Aggiungi Colonna")
        print("3. Elimina Colonna")
        print("4. Elimina Tabella")
        print("5. Inserisci Dati")
        print("6. Aggiorna Dati")
        print("7. Uscita")
        choice = input("Scegli un'opzione: ")
        
        if choice == '1':
            create_table(connection)
        elif choice == '2':
            add_column(connection)
        elif choice == '3':
            delete_column(connection)
        elif choice == '4':
            delete_table(connection)
        elif choice == '5':
            insert_data(connection)
        elif choice == '6':
            update_data(connection)
        elif choice == '7':
            print("Uscita...")
            break
        else:
            print("Opzione non valida, riprova.")

def main():
    connection = connect_to_mysql_server()
    if connection:
        database_name = input("Inserisci il nome del database da creare o a cui connettersi: ")
        conn_to_database(connection, database_name)
        manage_tables(connection)
        connection.close()
    else:
        print("Impossibile stabilire la connessione al server MySQL.")

if __name__ == "__main__":
    main()