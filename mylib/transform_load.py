"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv

#load the csv file and insert into a new sqlite3 database
def load(dataset = "data/central-park-raw.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('Centralpark.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Centralpark")
    c.execute("""
              CREATE TABLE Centralpark (,
              Max_TemperatureF INTEGER,
              Mean_TemperatureF INTEGER,
              Mean_Humidity REAL,
              CloudCover INTEGER,
              Events TEXT,
              EST TEXT
              )
              """)
    #insert

    c.executemany(
        """
        INSERT INTO Centralpark(
            Mean_TemperatureF, 
            Mean_Humidity,
            CloudCover, 
            Events,
            EST
            ) 
            VALUES (?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "Centralpark.db"