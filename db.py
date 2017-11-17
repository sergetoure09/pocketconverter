#import psycopg2
from lookup import retrieve_cur
import sqlite3

class Database:
    #local_path = "dbname='pocketDB' user='sergetoure' password='Footballeur1985#$' host='127.0.0.1' port='5432'"
    #heroku_path = "dbname='dc613q3o1fg3gg' user='qcwkaczdqghgzq' password='2395a876733ec5a349d54220f049006094166cadf5ee3ae2698da24d9778284b' host='ec2-54-221-225-114.compute-1.amazonaws.com' port='5432'"
    def __init__(self):
        print("Trying connection to database...")
        self.conn=sqlite3.connect("pocketdb")
        print("Connected successfully to database!")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS currency(cur_id INTEGER PRIMARY KEY AUTOINCREMENT,cur_label TEXT,cur_name TEXT)")
        self.conn.commit()
        self.cur.execute("CREATE TABLE IF NOT EXISTS  convert (convert_id INTEGER PRIMARY KEY AUTOINCREMENT,time_stamp TEXT,FOREIGN KEY(from_cur_id) REFRENCES currency(cur_id),FOREIGN KEY(to_cur_id) REFERENCES currency(cur_id),convert_rate DECIMAL,from_amount DECIMAL,to_amount DECIMAL)")
        self.conn.commit()
        print("Tables created or already existing in database")
        #self.conn.commit()

    def __del__(self):
        self.conn.close()
        print("Connection to database closed !") 
           
    def insert_currencies(self):
        currencies=retrieve_cur()["currencies"]
        for label,name in currencies.items():
            self.cur.execute('INSERT INTO currency (cur_label,cur_name) VALUES(label,name)')
            self.conn.commit()
            self.conn.close()
        
    def save_convert_request(self,time_stamp,from_cur_id,to_cur_id,convert_rate,from_amount,to_amount):
        self.cur.execute("INSERT INTO convert (time_stamp,from_cur_id,to_cur_id,convert_rate,from_amount,to_amount) VALUES(%s,%s,%s,%s,%s,%s)",(time_stamp,from_cur_id,to_cur_id,convert_rate,from_amount,to_amount))
        self.conn.commit()

    def ask_cur(self):
        self.cur.execute("SELECT * FROM currency")
        option_list=self.cur.fetchall()
        return option_list

mamassa = Database()
mamassa.insert_currencies()
#print(mamassa.ask_cur())




        
