#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Prueba-1 Python3
    Franco Friz Rodriguez
"""
import json
import urllib.request
from urllib.error import HTTPError


def get_api_data(url_string):
    """get_api_data: The function must take the json of type <key, value> 
    of the passed url as input, and return it as a list of tuples <key,value>

    Args:
        url String: #Unra url
    Retr:
        list of tuples: [(k, v) for k, v in x.items()]
    """
    try:
        with urllib.request.urlopen(url_string) as url:
            data = json.loads(url.read())
            #return data Json to List of Tuples [('','')]
            #Other method [(k, v) for k, v in data.items()]
            return list(data.items())
    except HTTPError as ex:
        print(ex.read())

def print_result(result):
    """Result print

    Args:
        result list of tuple: list of tuple JSON
    """
    print(json.dumps(result, indent=4))
        
def main():
    test1 = "https://invelonjobinterview.herokuapp.com/api/test1"
    test1_map = get_api_data(test1)
    print_result(test1_map)

    test2 = "https://invelonjobinterview.herokuapp.com/api/test2"
    test2_map = get_api_data(test2)
    print_result(test2_map)

if __name__ == "__main__":
    main()

