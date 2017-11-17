import psycopg2
from lookup import retrieve_cur

class Database:
    mypath = "dbname='pocketDB' user='sergetoure' password='Footballeur1985#$' host='127.0.0.1' port='5432'"
    def __init__(self):
        print("Trying connection to database...")
        self.conn=psycopg2.connect(self.mypath)
        print("Connected successfully to database!")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS currency (cur_id SERIAL NOT NULL ,cur_label TEXT,cur_name TEXT)")
        self.conn.commit()
        self.cur.execute("CREATE TABLE IF NOT EXISTS  convert (convert_id SERIAL NOT NULL ,time_stamp TEXT, from_cur_id INTEGER NOT NULL,to_cur_id INTEGER NOT NULL,convert_rate DECIMAL,from_amount DECIMAL,to_amount DECIMAL)")
        self.conn.commit()
        print("Tables created or already existing in database")
        #self.conn.commit()

    def __del__(self):
        self.conn.close()
        print("Connection to database closed !") 
           
    def insert_currencies(self):
        currencies=retrieve_cur()["currencies"]
        for label,name in currencies.items():
            self.cur.execute('INSERT INTO currency (cur_label,cur_name) VALUES(%s,%s)',(label,name))
            self.conn.commit()
        
    def save_convert_request(self,time_stamp,from_cur_id,to_cur_id,convert_rate,from_amount,to_amount):
        #self.cur.execute("SELECT cur_id from currency WHERE from_cur=")
        self.cur.execute("INSERT INTO convert (time_stamp,from_cur_id,to_cur_id,convert_rate,from_amount,to_amount) VALUES(%s,%s,%s,%s,%s,%s)",(time_stamp,from_cur_id,to_cur_id,convert_rate,from_amount,to_amount))
        self.conn.commit()

    def ask_cur(self):
        self.cur.execute("SELECT * FROM currency")
        option_list=self.cur.fetchall()
        return option_list

#mamassa = Database()
#mamassa.insert_currencies()
#print(mamassa.ask_cur())




        