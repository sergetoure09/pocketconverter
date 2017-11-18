from db import *
from lookup import *
from bokeh.plotting import figure
from bokeh.embed import components

class Controllers:
    def __init__(self):
        print("Starting controller...")
        self.db_conn=Database()

    def convert_control(self,from_cur,to_cur,from_amount):
        quote=retrieve_quote(from_cur[1],to_cur[1])# USD default keep in mind
        to_amount=float(quote[1])*float(from_amount)
        try:
            self.db_conn.save_convert_request(quote[0],from_cur[0],to_cur[0],quote[1],from_amount,to_amount)
            print("Search saved in database")
        except Exception as e:
                print("impossible d'enregistrer la recherche")
        
        return to_amount

    def option_cur(self):
        option_list=self.db_conn.ask_cur()
        return option_list

    def all_activities_control(self):
        data=self.db_conn.all_activities()
        return data
    
    def graph_control(self):
        x=[1,2,3,4]
        y=[5,25,37,17]
        p=figure(plot_width=500, plot_height=400,toolbar_location=None)
        p.hbar(y=x, height=0.5, left=0,
        right=y, color="navy")
        graph = components(p)
        return graph








