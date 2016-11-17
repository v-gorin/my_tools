#! /usr/bin/python
import argparse
import os

def new_path(old_path):
    return old_path.replace('\\','/')

def change_path(path, mnt):
    new_p = new_path(path)
    return mnt +'/' + new_p[new_p.find('log')+4:]

def cli():
    cli = argparse.ArgumentParser(prog="Programm summary",
                                description="Description")
    cli.add_argument('-p', '--old_path', type=str,
                     help='Show new format path')
    cli.add_argument('-m','--abs_mnt', type=str,
                     help='Abs path to mount point of smb')
    return cli.parse_args()

def main():
    args = cli()
    print change_path(args.old_path, args.abs_mnt) 

if __name__ == '__main__':
    main()
    
