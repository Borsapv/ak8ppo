import sqlite3

# connection to database
conn = sqlite3.connect("tajemnik.db")

# create cursor
c = conn.cursor()

# create tables predmety, zamestnanci, obory, stitek, vahy pacovnich bodu
c.execute(""" CREATE TABLE predmet (
    
    )
""")

c.execute(""" CREATE TABLE obor (
    
    )
""")

c.execute(""" CREATE TABLE predmet_obor (
    
    )
""")

c.execute(""" CREATE TABLE zamestnanec (
    name STRING, 
    last_name STRING,
    mail_work STRING,
    mail_private STRING,
    phone_number STRING,
    
    )
""")

c.execute(""" CREATE TABLE stitek (
    id INTEGER NOT NULL PRIMARY KEY
    )
""")

c.execute(""" CREATE TABLE vahy_pracovnich_bodu (
    id INTEGER NOT NULL PRIMARY KEY
    )
""")

#Commit commands
conn.commit()

#Close connection
conn.close()