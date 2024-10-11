# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1485841/behaviour-of-increment-and-decrement-operators-in-python
from l3.Runtime import _l_
def PreIncrement(name, local={}):
    _l_(2889)

    #Equivalent to ++name
    if name in local:
        _l_(2886)

        local[name]+=1
        _l_(2884)
        aux = local[name]
        _l_(2885)
        return aux
    globals()[name]+=1
    _l_(2887)
    aux = globals()[name]
    _l_(2888)
    return aux

def PostIncrement(name, local={}):
    _l_(2895)

    #Equivalent to name++
    if name in local:
        _l_(2892)

        local[name]+=1
        _l_(2890)
        aux = local[name]-1
        _l_(2891)
        return aux
    globals()[name]+=1
    _l_(2893)
    aux = globals()[name]-1
    _l_(2894)
    return aux

x = 1
_l_(2896)
y = PreIncrement('x') #y and x are both 2
_l_(2897) #y and x are both 2
a = 1
_l_(2898)
b = PostIncrement('a') #b is 1 and a is 2
_l_(2899) #b is 1 and a is 2

x = 1
_l_(2900)
def test():
    _l_(2904)

    x = 10
    _l_(2901)
    y = PreIncrement('x') #y will be 2, local x will be still 10 and global x will be changed to 2
    _l_(2902) #y will be 2, local x will be still 10 and global x will be changed to 2
    z = PreIncrement('x', locals()) #z will be 11, local x will be 11 and global x will be unaltered
    _l_(2903) #z will be 11, local x will be 11 and global x will be unaltered
test()
_l_(2905)

x = 1
_l_(2906)
print(PreIncrement('x'))   #print(x+=1) is illegal!
_l_(2907)   #print(x+=1) is illegal!

x = 1
_l_(2908)
x+=1
_l_(2909)
print(x)
_l_(2910)

def PreDecrement(name, local={}):
    _l_(2916)

    #Equivalent to --name
    if name in local:
        _l_(2913)

        local[name]-=1
        _l_(2911)
        aux = local[name]
        _l_(2912)
        return aux
    globals()[name]-=1
    _l_(2914)
    aux = globals()[name]
    _l_(2915)
    return aux

def PostDecrement(name, local={}):
    _l_(2922)

    #Equivalent to name--
    if name in local:
        _l_(2919)

        local[name]-=1
        _l_(2917)
        aux = local[name]+1
        _l_(2918)
        return aux
    globals()[name]-=1
    _l_(2920)
    aux = globals()[name]+1
    _l_(2921)
    return aux

