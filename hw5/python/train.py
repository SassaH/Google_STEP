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
        if station['Stations'] in st_lst:
            index = st_lst.index(station['Stations'])
            prev_lst = station['Prev'] + [st_lst[index]]
            if st_lst[index] != st_lst[-1]:
                next_st = st_lst[st_lst.index(station['Stations'])+1]
                if next_st not in station['Prev']:
                    next_lst.append({'Stations': next_st, 'Prev':prev_lst})
            if st_lst[index] != st_lst[0]:
                prev_st = st_lst[st_lst.index(station['Stations'])-1]
                if prev_st not in station['Prev']:
                    next_lst.append({'Stations': prev_st, 'Prev': prev_lst})
        i += 1
    return next_lst

def make_list(js, start, last):
    #q_lst = [{'Stations':start,'Prev':[]}]
    now_lst = [{'Stations':start,'Prev':[]}]
    next_lst = []
    judge = False
    while judge == False:
        index = 0
        while index < len(now_lst):
            #q_lst.append(serch_next(js, now_lst[index]))
            next_lst = next_lst + serch_next(js, now_lst[index])
            for i in range(0,len(now_lst)):
                if last in now_lst[i]['Stations'] :
                    ans = now_lst[i]
                    judge = True
                    break
                i += 1
            index += 1
        now_lst = copy.deepcopy(next_lst)
        del next_lst[:]
        if now_lst == [{'Prev': [u'Seaside Beach', u'Mount Jub-Jub', u'White Manor'], 'Stations': u'Nowhere'}]:
            ans = {'Stations':'error','Prev':['error']}
            judge = True
    print ans['Prev']
    return ans['Prev']
    
make_list(js,'Seaside Beach', "Tulgey Wood")
#print serch_next(js, {'Prev': ['Seaside Beach'], 'Stations': 'Mount Jub-Jub'})
#print serch_next(js, {'Prev': [], 'Stations':'Seaside Beach'})
#print serch_next(js, {'Prev': ['Seaside Beach', u'Mount Jub-Jub'], 'Stations': u'Field of Flying Elephants'})
