from typing import List # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/18265935/how-do-i-create-a-list-with-numbers-between-two-values
from l3.Runtime import _l_
start=0
_l_(13940)
end=10
_l_(13941)
arr=list(range(start,end+1))
_l_(13942)
output: arr=[0,1,2,3,4,5,6,7,8,9,10]
_l_(13943)

ar=[]
_l_(13944)
def diff(start,end):
    _l_(13950)

    if start==end:
        _l_(13949)

        d.append(end)
        _l_(13945)
        aux = ar
        _l_(13946)
        return aux
    else:
        ar.append(end)
        _l_(13947)
        aux = diff(start-1,end) 
        _l_(13948) 
        return aux 

