from abc import ABC, abstractmethod

# Interfaccia astratta per qualsiasi gestore di database
class DatabaseManagerBase(ABC):
    
    # Connessione al server/database
    @abstractmethod
    def connect(self):
        pass

    # Creazione di un database
    @abstractmethod
    def create_database(self, name):
        pass

    # Connessione a un database esistente
    @abstractmethod
    def connect_to_database(self, name):
        pass

    # Creazione tabella
    @abstractmethod
    def create_table(self):
        pass

    # Aggiunta colonna
    @abstractmethod
    def add_column(self):
        pass

    # Eliminazione colonna
    @abstractmethod
    def delete_column(self):
        pass

    # Eliminazione tabella
    @abstractmethod
    def delete_table(self):
        pass

    # Inserimento dati
    @abstractmethod
    def insert_data(self):
        pass

    # Aggiornamento dati
    @abstractmethod
    def update_data(self):
        pass
