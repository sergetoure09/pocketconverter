from db import *
from lookup import *

class controllers:
    def __init__(self):
        print("Starting controller...")
        self.db_conn=Database()

    def convert(self,from_cur,to_cur,from_amount):
        quote=retrieve_quote(from_cur[1],to_cur[1])# USD default keep in mind
        to_amount=float(quote[1])*float(from_amount)
        self.db_conn.save_convert_request(quote[0],from_cur[0],to_cur[0],quote[1],from_amount,to_amount)





