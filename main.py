from concrete_database_manager import MySQLDatabaseManager


def main():
    # Crea l'istanza del gestore MySQL
    manager = MySQLDatabaseManager(password="Allitterazione0098") # la password è personale 
    manager.connect()

    # Connessione o creazione database
    db_name = input("Nome del database: ")
    manager.connect_to_database(db_name)

    # Menu interattivo
    while True:
        print("\nMenu:")
        print("1. Crea tabella")
        print("2. Aggiungi colonna")
        print("3. Elimina colonna")
        print("4. Elimina tabella")
        print("5. Inserisci dati")
        print("6. Aggiorna dati")
        print("7. Esci")

        choice = input("Scelta: ")

        match choice:
            case "1":
                manager.create_table()
            case "2":
                manager.add_column()
            case "3":
                manager.delete_column()
            case "4":
                manager.delete_table()
            case "5":
                manager.insert_data()
            case "6":
                manager.update_data()
            case "7":
                print("Uscita.")
                break
            case _:
                print("Opzione non valida.")

    # Chiude la connessione al database
    if manager.connection.is_connected():
        manager.connection.close()

if __name__ == "__main__":
    main()
