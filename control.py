from db import *
from lookup import *

class Controllers:
    def __init__(self):
        print("Starting controller...")
        self.db_conn=Database()

    def convert(self,from_cur,to_cur,from_amount):
        quote=retrieve_quote(from_cur[1],to_cur[1])# USD default keep in mind
        to_amount=float(quote[1])*float(from_amount)
        self.db_conn.save_convert_request(quote[0],from_cur[0],to_cur[0],quote[1],from_amount,to_amount)
        return to_amount

    def option_cur(self):
        option_list=self.db_conn.ask_cur()
        return option_list







