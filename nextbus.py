#!/usr/bin/python3
import argparse
import requests
import json
import logging
import time
import os

logging.basicConfig(level=logging.INFO)


SVC_URL = "https://svc.metrotransit.org"
ENV_SVC_URL_KEY = 'SVC_URL' 
if ENV_SVC_URL_KEY in os.environ:
    SVC_URL=os.environ[ENV_SVC_URL_KEY]
SVC_RESPONSE_FORMAT = "format=json"


def check_main_service_healthcheck(SVC_URL):
    """ Check the main service url health. Returns True of False based on HTTP response code"""
    try:
        r =requests.get(SVC_URL+'/NexTrip')
        if r.status_code ==200:
            return True
        else:
            return False
    except Exception as e:
        return False


def call_webservice(url):
    """ calls HTTP get method on particular webservice URL"""
    try:
        r =requests.get(url)
        return r
    except Exception as e:
        return e



def find_route_info_by_name(busroute):
    """ returns route information by route name"""

    constructing_string_url=SVC_URL+'/NexTrip/Routes?'+SVC_RESPONSE_FORMAT
    r=call_webservice(constructing_string_url)
    if r.status_code ==200:
        route_dict = json.loads(r.text)
        for route in route_dict:
            if route['Description'].lower().strip()==busroute.lower().strip():
                logging.debug("valid response: find_route_info_by_name method : "+str(route))
                return route
        return None
    return None

def get_direction_id_by_route_id(route_id, direction):
    """ returns direction id  information by route id"""
    constructing_string_url=SVC_URL+'/NexTrip/Directions/'+str(route_id)+'?'+SVC_RESPONSE_FORMAT
    r=call_webservice(constructing_string_url)
    if r.status_code ==200:
        direction_dict = json.loads(r.text)
        for direction_data in direction_dict:
            if direction.lower() in direction_data['Text'].lower():
                logging.debug("valid response: get_direction_id_by_route_id method : "+str(direction_data['Value']))
                return str(direction_data['Value'])
        return None
    return None

def get_stop_code_by_route_and_direction_ids(route_id, direction_id, busstop):
    """ returns stop code information from route and direction"""

    constructing_string_url=SVC_URL+'/NexTrip/Stops/'+str(route_id)+'/'+str(direction_id)+'?'+SVC_RESPONSE_FORMAT
    r =call_webservice(constructing_string_url)
    if r.status_code ==200:
        stop_dict = json.loads(r.text)
        for stop in stop_dict:
            if stop['Text'].lower().strip()==busstop.lower().strip():
                logging.debug("valid response: get_stop_code_by_route_and_direction_ids method : "+str(stop['Value']))
                return str(stop['Value'])
        return None
    return None

def get_wait_time_for_next_bus(route_id,direction_id,get_stop_code):
    """ returns the get wait time for the next bus in Minutes using route id, direction id and stop code """
    constructing_string_url=SVC_URL+'/NexTrip/'+str(route_id)+'/'+str(direction_id)+'/'+str(get_stop_code)+'?'+SVC_RESPONSE_FORMAT
    r =call_webservice(constructing_string_url)
    logging.debug("final url  : "+constructing_string_url)
    if r.status_code ==200:
        next_bus_dict = json.loads(r.text)
        if len(next_bus_dict) > 0:
            if 'Min' in next_bus_dict[0]['DepartureText']:
                waittime = str(next_bus_dict[0]['DepartureText']).replace("Min", "Minutes")
                return waittime
            else:
                logging.debug("Next Bus at: "+next_bus_dict[0]['DepartureText'])
                nextbustimestamp=next_bus_dict[0]['DepartureTime']
                current_time = time.time()
                nextbustimestamp = nextbustimestamp.replace("/Date(", "")
                nextbustimestamp = nextbustimestamp.replace("-0600)/", "")
                waittime = str(round(((float(nextbustimestamp)/1000) - current_time) / 60.0)) + " Minutes"
                logging.debug("Wait time in minutes:"+waittime)
                return waittime
        else:
            return "No bus available today for the destination"

def nextbusinfo(busroute, busstop, direction):
    """ returns wait time information from user input information """
    routeinfo = find_route_info_by_name(busroute)
    if(type(routeinfo)==dict):
        logging.debug(routeinfo['Description'])
        route_id=routeinfo['Route']
        direction_id=get_direction_id_by_route_id(route_id, direction)
        if direction_id is not None:
            get_stop_code=get_stop_code_by_route_and_direction_ids(route_id, direction_id, busstop)
            if get_stop_code is not None:
                wait_time=get_wait_time_for_next_bus(route_id,direction_id,get_stop_code)
                return "Wait Time : "+wait_time
            else:
                return "Response: stop not found"
        else:
            return "Response: direction not found"
    else:
        return "Response:route not found"

parser  = argparse.ArgumentParser('''
This script returns the  Wait time for your next bus.  

Example usage: 
python3 nextbus.py "METRO Blue line" "Target Field Station Platform 1" "south"


''')
parser.add_argument('busroute',type = str,  help="provide the bus route name, for example \'METRO Blue Line\'")
parser.add_argument('busstop', type = str, help="provide the bus stop name, for example \'Target Field Station Platform 1\'")
parser.add_argument('direction', type = str,  help="provide direction of the route, for example \'south\'", choices=['south', 'north', 'east', 'west'] )

if __name__ == '__main__':

    try:
        args = parser.parse_args()
        print("\n")
        print("-----------Input request information-------")
        print("Route: "+str(args.busroute))
        print("Stop: "+str(args.busstop))
        print("Direction: "+str(args.direction))    
        if check_main_service_healthcheck(SVC_URL):
            pass
        else:
            print("main service health checks")
            exit()
        busroute=str(args.busroute).lower().strip()
        busstop=str(args.busstop).lower().strip()
        direction=str(args.direction).lower().strip()
        response=nextbusinfo(busroute, busstop, direction)
        print(response)
        print("------Script completed--------")
        print("\n\n")
    except Exception as e:
        print(e)
        




    

