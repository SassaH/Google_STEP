# -*- coding: utf-8 -*-
import urllib
import json
import copy


res = urllib.urlopen('http://alice.fantasy-transit.appspot.com/net?format=json')
js = json.load(res)
#repr(js).decode("unicode-escape")


#となり駅の情報をリストにする
def serch_next(js, station): 
    next_lst = []
    for i in range(0,len(js)):
        st_lst = js[i]['Stations']
        dis = station['Length']+1
        if  station['Staitions'] in st_lst:
            if st_lst not in station['Prev']:
                prev_lst = stations['Prev'] + [st_lst[index]]
                index = st_lst.index(station)
                if st_lst[index] != st_lst[-1]:
                    next_lst.append({'Stations':st_lst[st_lst.index(station)+1], 'Length': dis, 'Prev':prev_lst})
                if st_lst[index] != st_lst[0]:
                    next_lst.append({'Stations':st_lst[st_lst.index(station)-1], 'Length': dis, 'Prev': prev_lst})
            i += 1
    return next_lst

def make_list(js, start, last):
    q_lst = [{'Stations':start,'Length':0,'Prev':[]}]
    now_lst = [start]
    while 1:
        index = 0
        while index < len(now_lst):
            next_station = serch_next(js, now_lst[index])
            q_lst.append(next_station)
            now_lst = next_station
            index += 1
            for i in range(0,len(now_lst)):
                if last in now_lst[i]['Stations'] :
                    ans = now_lst[i]
                    break
                    i += 1
    print ans['Prev']
    
make_list(js, "Seaside Beach", "Tulgey Wood")
#print serch_next(js, "Seaside Beach")

