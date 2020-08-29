#!/bin/usr/env python
# -*- coding: utf-8 -*-
import sys
import os
import json


def check_position(check_dir_num=-2):
    pwd = os.getcwd()
    items = pwd.split('/')
    if not items[check_dir_num] == 'projects':
        print('execute this just under /path/to/projects/project_name/')
        exit()

    return


def extract_common_dir(pre_dir_lst):
    dir_lst = []
    for tmpdir in pre_dir_lst:
        items = tmpdir.split('/')
        n_elm = len(items)
        dir_lst.append('/'.join(items[:n_elm-1]))

    return dir_lst


def get_dirs(server_home):
    pwd = os.getcwd()
    dir_lst = pwd.split('/')
    pos = dir_lst.index('projects')

    dir_dict = {}

    #prog_dir = '/'.join(dir_lst[:pos+2])
    prog_dir = '/'.join(dir_lst[:])
    dir_dict['from'] = prog_dir

    #exc_home_dir = '/'.join(dir_lst[pos:pos+2])
    exc_home_dir = '/'.join(dir_lst[pos:])
    dir_dict['to'] = os.path.join(server_home, exc_home_dir)

    home_dir = '/'.join(dir_lst[:pos])
    dir_dict['home'] = home_dir

    return dir_dict


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


def check_exist_server_file(script_path):
    server_dict_path = os.path.join(script_path, '../data/server.json')

    if not os.path.exists(server_dict_path):
        server_dict_template_path = os.path.join(script_path, '../data/server_template.json')
        print('Make %s using %s as reference'%(server_dict_path, server_dict_template_path))
        exit()

    return


def get_server_list():
    script_path = os.path.dirname(os.path.abspath(__file__))
    check_exist_server_file(script_path)
    server_dict_path = os.path.join(script_path, '../data/server.json')

    with open(server_dict_path, 'r') as f:
        server_dict = json.load(f)

    return server_dict


def get_parse():
    args = sys.argv

    if(len(args) < 4):
        print('usage: $ script.py sync_dir [to|from] server [mode]')
        exit()

    sync_dir = args[1]
    direct = args[2]
    server = args[3]

    mode = 'normal'
    if len(args) == 5:
        mode = args[4]

    args = {}
    if mode == 'analysis':
        args['sync_dir'] = 'analysis'
        args['direct'] = 'from'
    elif mode == 'analysis_man':
        args['sync_dir'] = 'analysis_man'
        args['direct'] = 'from'
    else:
        args['sync_dir'] = sync_dir
        args['direct'] = direct
    args['server'] = server
    args['mode'] = mode

    return args


def main():
    return


if __name__ == "__main__":
    main()
