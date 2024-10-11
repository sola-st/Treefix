# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe
from l3.Runtime import _l_
try:
    import pandas as pd
    _l_(1308)

except ImportError:
    pass

df = pd.DataFrame({'ID':['1','2','3'], 'col_1': [0,2,3], 'col_2':[1,4,5]})
_l_(1309)
mylist = ['a','b','c','d','e','f']
_l_(1310)

def get_sublist(sta,end):
    _l_(1312)

    aux = mylist[sta:end+1]
    _l_(1311)
    return aux

def get_sublist_list(cols):
    _l_(1314)

    aux = [get_sublist(cols[0],cols[1])]
    _l_(1313)
    return aux

def unlist(list_of_lists):
    _l_(1316)

    aux = list_of_lists[0]
    _l_(1315)
    return aux

df['col_3'] = df[['col_1','col_2']].apply(get_sublist_list,axis=1).apply(unlist)
_l_(1317)

df
_l_(1318)

