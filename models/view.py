import mysql.connector

class View:
    def __init__(self):
        self.host="localhost",
        self.user="root",
        self.password="1234",
        self.database = 'Recipe'

    def fetch(self, name):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database = 'Recipe'
            )
        sql = f"SELECT * FROM recipes WHERE name = '{name}'" 
        
        cursor = mydb.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        for row in records:
            time = row[2]
            ing = row[3]
            ins = row[4]
            notes = row[5]
        return [time, ing,ins, notes]
        mydb.commit()
        cursor.close()
        mydb.close()