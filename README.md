# File sync
Synchronizes files in current server with those in another server.

## Work
### Synchronize
This program synchronizes directories under `/path/to/projects/<project name>/`.

Type of synchronizing directories are two:

(1) choiced directory as synchronizing_directory in usage, and

(2) common use directories written in
`/path/to/projects/<project name>/common/sync/commondir.txt` in each line.

### Server
Server information with its home directory of project in json format is put at 
`/path/to/file_sync/data/server.json`.
To connect `~/.ssh/config` is used.

## Usage
Execute this program just under `/path/to/projects/<project name>/` as

    $ python source/main.py [to|from] server synchronizing_directory

"to" is for synchronizing directories in current server to "server",
and "from" is for the anti-direction.

## Requarement
paramiko

