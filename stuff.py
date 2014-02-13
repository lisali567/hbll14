# _*_ coding: utf-8 _*_

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

player_stuff = {'원': 2, '사람':1, '김치':3, '건물':1, '양':0, '양모':0, '소':0, '우유':0, '나무':0}

def add_inventory(thing, plus_num):
    player_stuff[thing] += plus_num

def subtract_inventory(thing, minus_num):
    player_stuff[thing] -= minus_num

