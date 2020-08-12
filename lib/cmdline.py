import argparse
import sys


def banner():
    banner_str = """\033[01;31m                                  ______
                                 / ____| 
     _____     _____     ______ | (____     ______   _____   ______
    / ___ \   / ___ \   / ____/  \_____ \  / ____/  / __  | | ____ |
   / /__/ /  / /__/ /  / /____    ____) | / /____  | (__| | | |  | |
  / /____/   \_____/   \_____/   |______/ \_____/   \ ____| | |  | |
 / /                             \033[0mauthor:https://github.com/medasz
\033[01;31m/ /                              \033[0mvulnerability Scanner
"""
    print(banner_str, end="")


def parse_args():
    parse = argparse.ArgumentParser(prog='pocScan', description='vulnerability Scanner', usage='pocScan [options]')
    parse.add_argument('-u', '--url', help='Scan several url from command line', type=str, metavar='url', nargs="*",
                       default="")
    parse.add_argument('-f', '--file', help='Load new line delimited targets from TargetFile', type=str,
                       metavar='TargetFile', default="")
    parse.add_argument('-p', '--plugin', help='Load plugins from TargetDirectory', metavar='TargetDirectory', type=str,
                       default='plugin')
    if len(sys.argv) == 1:
        parse.print_help()
    argv = parse.parse_args()
    return argv
