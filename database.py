import mysql.connector

#connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="testovaciHeslo1*",
    database="tajemnik"
)

#create a cursor
c = mydb.cursor()

#create database - once
#c.execute("CREATE DATABASE tajemnik")

#create a table if not exists
def create_tables():
    c.execute("CREATE TABLE IF NOT EXISTS zamestnanci (\
        empl_id INT AUTO_INCREMENT PRIMARY KEY,\
        first_name VARCHAR(255),\
        last_name VARCHAR(255), \
        work_mail VARCHAR(255), \
        private_mail VARCHAR(255), \
        phone_number VARCHAR(15), \
        doctoral BOOL, \
        work_load FLOAT)")

    c.execute("CREATE TABLE IF NOT EXISTS courses (\
        course_id INT AUTO_INCREMENT PRIMARY KEY, \
        course_abbr VARCHAR(255), \
        course_name VARCHAR(255), \
        weeks INT(3), \
        hours_p INT (3), \
        hours_c INT (3), \
        hours_s INT (3), \
        completion_type VARCHAR(255), \
        language VARCHAR(2), \
        max_students INT(4))")

    c.execute("CREATE TABLE IF NOT EXISTS stitky (\
        stitek_id INT AUTO_INCREMENT PRIMARY KEY, \
        empl_id INT, FOREIGN KEY(empl_id) REFERENCES zamestnanci(empl_id),  \
        course_name VARCHAR(255), \
        name VARCHAR(255), \
        course_type VARCHAR(255), \
        language VARCHAR(255), \
        hours INT(3), \
        completion_type VARCHAR(255), \
        students INT(3))")


def drop_tables():
    c.execute("DROP TABLE IF EXISTS zamestnanci, courses, stitky")

def show_tables():
    c.execute("SHOW TABLES")
    tables = c.fetchall()
    print(tables)

def show_table_description():
    c.execute("SELECT * FROM zamestnanci")
    print(c.description)

drop_tables()
create_tables()
show_tables()


mydb.commit()
mydb.close

