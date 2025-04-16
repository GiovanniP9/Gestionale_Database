# MySQL Database Manager in Python

Un semplice tool da riga di comando per connettersi a un server MySQL, gestire database, tabelle e dati, scritto in Python. Progettato con un'architettura modulare che include astrazione, classi concrete e gestione pulita degli errori.

## Funzionalità

- Connessione al server MySQL
- Creazione e selezione di database
- Creazione di tabelle personalizzate
- Aggiunta ed eliminazione di colonne
- Eliminazione di tabelle
- Inserimento e aggiornamento dati

## Struttura del Progetto
```
mysql-database-manager/
│
├── src/
│   ├── main.py                      # Entry point
│   ├── abstract_database_manager.py # Interfaccia astratta
│   ├── concrete_database_manager.py # Implementazione concreta con MySQL
│
├── README.md
└── requirements.txt
```

## Documentazione
- Giovanni si è occupato della scrittura dei methodi della classe `MySQLDatabaseManager` e della corretta implementazione dei metodi della classe nel menù di esecuzione, oltre alla fase di visualizzazione del Database tramite WorkBench;
- Nunzio si è occupato della separazione della logica funzionale per rendere il progetto modulare, leggibile, e manutenibile, e della scrittura dell'interfaccia astratta `DatabaseManagerBase` per la classe di Giovanni.
  
## Requisiti

- Python 3.8+
- MySQL Server installato e in esecuzione
- Pacchetti Python:
  - `mysql-connector-python`

Installa i requisiti con:

```bash
pip install mysql-connector-python
