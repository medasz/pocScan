# -*- coding: utf-8 -*-
from lib.cmdline import banner, parse_args
from lib.framework import framework
from lib.utils.PrettyTable import PrettyTable

if __name__ == '__main__':
    banner()
    argv = parse_args()

    frame = framework(argv.url, plugin=argv.plugin)
    frame.exploit()

    table = PrettyTable()
    table.field_names = ['url', 'poc', 'success', 'info']
    for x in frame.result:
        table.add_row(x)
    print(table)
    print('success : {}'.format(len(frame.result)))
