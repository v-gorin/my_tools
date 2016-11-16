#! /usr/bin/python
import argparse
import os

def new_path(old_path):
    return old_path.replace('\\','/')

def change_path(path):
    new_p = new_path(path)
    return os.path.abspath('apps_' + new_p[new_p.find('log'):])

def cli():
    cli = argparse.ArgumentParser(prog="Programm summary",
                                description="Description")
    cli.add_argument('-p', '--old_path', type=str,
                     help='Show new format path')
    return cli.parse_args()

def main():
    args = cli()
    print change_path(args.old_path) 

if __name__ == '__main__':
    main()
    
