import sqlite3

# connection to database
conn = sqlite3.connect("tajemnik.db")
conn.execute("PRAGMA foreign_keys = 1")

# create cursor
c = conn.cursor()

# create tables predmety, zamestnanci, obory, stitek, vahy pacovnich bodu
c.execute(""" CREATE TABLE predmet (
    id_subject INTEGER PRIMARY KEY NOT NULL,
    name STRING,
    pocet_hodin INTEGER,
    id_employee INTEGER NOT NULL,
    FOREIGN KEY (id_employee)
        REFERENCES zamestnanec(id_employee)
        ON UPDATE CASCADE
        ON DELETE RESTRICT    
    )
""")

c.execute(""" CREATE TABLE obor (
    id INTEGER
    )
""")

c.execute(""" CREATE TABLE predmet_obor (
    id INTEGER
    )
""")

c.execute(""" CREATE TABLE zamestnanec (
    id_employee INTEGER PRIMARY KEY NOT NULL,
    name STRING, 
    last_name STRING,
    mail_work STRING,
    mail_private STRING,
    phone_number STRING
    
    )
""")

c.execute(""" CREATE TABLE stitek (
    id INTEGER
    )
""")

c.execute(""" CREATE TABLE vahy_pracovnich_bodu (
    id INTEGER
    )
""")

#Commit commands
conn.commit()

#Close connection
conn.close()