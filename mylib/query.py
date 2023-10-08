"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"

def log_query(query):
        """adds to a query markdown file"""
        with open(LOG_FILE, "a") as file:
            file.write(f"```sql\n{query}\n```\n\n") 

def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("Centralpark.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")

def create_record(
    Mean_TemperatureF,Mean_Humidity,CloudCover,Events,EST
):
    """create example query"""
    conn = sqlite3.connect("Centralpark.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO Centralpark 
        (
        Mean_TemperatureF, 
        Mean_Humidity, 
        CloudCover, 
        Events, 
        EST) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (
         Mean_TemperatureF, 
         Mean_Humidity, 
         CloudCover, 
         Events, 
         EST),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO Centralpark VALUES (
            {Mean_TemperatureF}, 
            {Mean_Humidity}, 
            {CloudCover},
            {Events},
            {EST},);"""
    )


def update_record(
    Max_TemperatureF, Mean_TemperatureF, Mean_Humidity, CloudCover, Events, EST
):
    """update example query"""
    conn = sqlite3.connect("Centralpark.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE Centralpark 
        SET Mean_TemperatureF=?, 
        Mean_Humidity=?, CloudCover=?, 
        Events=?, 
        EST = ?,
        WHERE Max_TemperatureF=?
        """,
        (
            Mean_TemperatureF, Mean_Humidity, CloudCover, Events, EST, Max_TemperatureF
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE Centralpark SET 
        Mean_TemperatureF=
        {Mean_TemperatureF},
        Mean_Humidity={Mean_Humidity}, CloudCover={CloudCover}, 
        Events={Events}, 
        WHERE Max_TemperatureF={Max_TemperatureF};"""
    )


def delete_record(Max_TemperatureF):
    """delete example query"""
    conn = sqlite3.connect("Centralpark.db")
    c = conn.cursor()
    c.execute("DELETE FROM Centralpark WHERE Max_TemperatureF=?", (Max_TemperatureF,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM Centralpark WHERE Max_TemperatureF={Max_TemperatureF};")


def read_data():
    """read data"""
    conn = sqlite3.connect("Centralpark.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Centralpark")
    data = c.fetchall()
    log_query("SELECT * FROM Centralpark;")
    return data


