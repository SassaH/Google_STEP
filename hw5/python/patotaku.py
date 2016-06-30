# -*- coding: utf-8 -*-

def combine(str1, str2):
    ans = ""
    #i = 0
    str_len = max(len(str1), len(str2))
    for i in range(0, str_len):
        ans = ans + str1[i:i+1] + str2[i:i+1]
    #ans = ans + str[str_len:]
    return ans

print combine("cat","dog")
        
