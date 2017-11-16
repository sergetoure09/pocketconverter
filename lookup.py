import requests
import json
import datetime

API_key='a4514772540dcd2cf35989b792ecf667'
API_request='http://apilayer.net/api/'
ENDPOINT_list='list'
ENDPOINT_convert='live'
geek='?access_key='

def retrieve_cur():
    data=requests.get(API_request+ENDPOINT_list+geek+API_key)
    #print(API_request+API_key)
    data=data.content
    data=json.loads(data)
    for k,v in data["currencies"].items():
        print(k,v)
def convert_time_stamp(time_stamp):
    timy=datetime.datetime.fromtimestamp(int(time_stamp)).strftime('%Y-%m-%d %H:%M:%S')
    return timy
def retrieve_quote(from_cur,to_cur):
    data=requests.get(API_request+ENDPOINT_convert+geek+API_key+'&from='+from_cur+'&to='+to_cur)
    print(API_request+ENDPOINT_convert+geek+API_key+'&currencies='+to_cur)
    data=data.content
    data=json.loads(data)
    time_stamp=convert_time_stamp(data['timestamp'])
    return (time_stamp,data['quotes']['USD'+to_cur]) #default is USD my plan is bad need to change that ASAP

print(retrieve_quote('XOF','MAD'))



#print(convert_time_stamp("1284101485"))