#!/bin/usr/env python
# -*- coding: utf-8 -*-
import paramiko
import subprocess
import os
from directory import get_dirs
from IO import get_file_data_as_list


def make_basedir(dir_dict, server, system):
    dir_lst = get_file_data_as_list(dir_dict['from'] + '/common/setting/basedir.txt')

    config_file = dir_dict['home'] + '/.ssh/config'
    ssh_config = paramiko.SSHConfig()
    ssh_config.parse(open(config_file, 'r'))
    lkup = ssh_config.lookup(server)
    with paramiko.SSHClient() as ssh:
        ssh.load_system_host_keys()
        ssh.connect(
            hostname=lkup['hostname'], username=lkup['user'],
            key_filename=lkup['identityfile']
        )

        for dir_tmp in dir_lst:
            path = os.path.join(dir_dict['to'], dir_tmp)
            ssh.exec_command('mkdir -p ' + path)

        path = os.path.join(dir_dict['to'], system)
        ssh.exec_command('mkdir -p ' + path)

    return


def rsync_to(dir_dict, server, system):

    # common dir
    dir_lst = get_file_data_as_list(dir_dict['from'] + '/common/setting/commondir.txt')
    dir_lst.append(system)
    for dir_tmp in dir_lst:
        from_dir = os.path.join(dir_dict['from'], dir_tmp) + '/'
        to_dir = os.path.join(dir_dict['to'], dir_tmp)

        cmd = 'rsync -av %s %s:%s'%(from_dir, server, to_dir)
        subprocess.run(cmd.split())

    return


def rsync_from(dir_dict, server, system):

    # common dir
    dir_lst = get_file_data_as_list(dir_dict['from'] + '/common/setting/commondir.txt')
    dir_lst.append(system)
    for dir_tmp in dir_lst:
        from_dir = os.path.join(dir_dict['from'], dir_tmp)
        to_dir = os.path.join(dir_dict['to'], dir_tmp) + '/'
        cmd = 'rsync -av %s:%s %s'%(server, to_dir, from_dir)

        subprocess.run(cmd.split())

    return


def rsync_main(direct, server, system, server_home):

    dir_dict = get_dirs(server_home)

    if direct == 'to':
        make_basedir(dir_dict, server, system)
        rsync_to(dir_dict, server, system)
    elif direct == 'from':
        rsync_from(dir_dict, server, system)

    return


def main():
    return


if __name__ == "__main__":
    main()