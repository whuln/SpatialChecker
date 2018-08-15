# -*- coding: utf-8 -*-

#按行列输出list
def print_list_row_col(list, row):
    if len(list) == 0:
        return '无'

    _list = list
    r = row
    result = ''
    count = len(_list)
    index = 0
    for item in _list:
        result += item +'  '
        index = index + 1
        if((index+1) % r == 0):
            result += '\n'
    return result