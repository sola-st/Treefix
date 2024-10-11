# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe
from l3.Runtime import _l_
try:
    import pandas as pd
    _l_(12979)

except ImportError:
    pass

df = pd.DataFrame({'ID':['1','2','3'], 'col_1': [0,2,3], 'col_2':[1,4,5]})
_l_(12980)
mylist = ['a','b','c','d','e','f']
_l_(12981)

def get_sublist(sta,end):
    _l_(12983)

    aux = mylist[sta:end+1]
    _l_(12982)
    return aux

def get_sublist_list(cols):
    _l_(12985)

    aux = [get_sublist(cols[0],cols[1])]
    _l_(12984)
    return aux

def unlist(list_of_lists):
    _l_(12987)

    aux = list_of_lists[0]
    _l_(12986)
    return aux

df['col_3'] = df[['col_1','col_2']].apply(get_sublist_list,axis=1).apply(unlist)
_l_(12988)

df
_l_(12989)

