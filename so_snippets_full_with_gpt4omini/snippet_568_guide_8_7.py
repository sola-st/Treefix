# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/18265935/how-do-i-create-a-list-with-numbers-between-two-values
from l3.Runtime import _l_
start=0
_l_(1782)
end=10
_l_(1783)
arr=list(range(start,end+1))
_l_(1784)
output: arr=[0,1,2,3,4,5,6,7,8,9,10]
_l_(1785)

ar=[]
_l_(1786)
def diff(start,end):
    _l_(1792)

    if start==end:
        _l_(1791)

        d.append(end)
        _l_(1787)
        aux = ar
        _l_(1788)
        return aux
    else:
        ar.append(end)
        _l_(1789)
        aux = diff(start-1,end) 
        _l_(1790) 
        return aux 

