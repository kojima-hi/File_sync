#!/bin/usr/env python
# -*- coding: utf-8 -*-
import sys
import os
import json


def get_file_data_as_list(fname):
    lst = []
    with open(fname, 'r') as f:
        for string in f:
            lst.append(string.strip())
    return lst


def check_args(args, server_lst):

    direct_lst = ['to', 'from']
    if not args['direct'] in direct_lst:
        print('%s is invalid as direction.'%args['direct'])
        exit()

    if not args['server'] in server_lst:
        print('%s is invalid as server.'%args['server'])
        exit()

    return


def get_server_list():
    script_path = os.path.dirname(os.path.abspath(__file__))
    command_dict_path = os.path.join(script_path, '../data/server.json')

    with open(command_dict_path, 'r') as f:
        server_dict = json.load(f)

    return server_dict


def get_parse():
    args = sys.argv

    if(len(args) < 4):
        print('usage: $ script.py [to|from] server system')
        exit()

    direct = args[1]
    server = args[2]
    system = args[3]

    args = {}
    args['direct'] = direct
    args['server'] = server
    args['system'] = system

    return args


def main():
    return


if __name__ == "__main__":
    main()
