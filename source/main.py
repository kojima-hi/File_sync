#!/bin/usr/env python
# -*- coding: utf-8 -*-
from IO import get_parse, get_server_list, check_args, check_position
from rsync import rsync_main


def main():
    # get arguments
    args = get_parse()
    server_dict = get_server_list()

    # check position
    mode = args['mode']
    check_dir_num = -2
    if mode == 'analysis' or mode == 'analysis_man':
        check_dir_num = -4
    check_position(check_dir_num)
    del args['mode']

    server_lst = server_dict.keys()
    check_args(args, server_lst)

    server_home = server_dict[args['server']]
    args['server_home'] = server_home

    rsync_main(**args)

    return


if __name__ == "__main__":
    main()
