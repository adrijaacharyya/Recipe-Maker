import mysql.connector

class Creation:
    def __init__(self):
        self.host="localhost",
        self.user="root",
        self.password="1234",
        self.database = 'Recipe'

    def insert(self, dict):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database = 'Recipe'
            )
        mycursor = mydb.cursor()
        sql = "INSERT INTO recipes(name, time, ingredient, instructions, notes) VALUES (%s, %s, %s, %s, %s)"
        name = dict['name']
        time = dict['time']
        ingredient = dict['ing-name']
        ins = dict['instructions']
        notes = dict['notes']

        # val = (dict['name'], dict['time'], dict['ing-name'], dict['instructions'], dict['notes'])
        val = (name, time, ingredient, ins, notes)
        print('look',val)
       
        mycursor.execute(sql, list(dict.values()))
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        mydb.close()

