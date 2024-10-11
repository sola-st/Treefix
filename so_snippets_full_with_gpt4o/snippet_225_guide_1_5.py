# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1485841/behaviour-of-increment-and-decrement-operators-in-python
from l3.Runtime import _l_
def PreIncrement(name, local={}):
    _l_(14618)

    #Equivalent to ++name
    if name in local:
        _l_(14615)

        local[name]+=1
        _l_(14613)
        aux = local[name]
        _l_(14614)
        return aux
    globals()[name]+=1
    _l_(14616)
    aux = globals()[name]
    _l_(14617)
    return aux

def PostIncrement(name, local={}):
    _l_(14624)

    #Equivalent to name++
    if name in local:
        _l_(14621)

        local[name]+=1
        _l_(14619)
        aux = local[name]-1
        _l_(14620)
        return aux
    globals()[name]+=1
    _l_(14622)
    aux = globals()[name]-1
    _l_(14623)
    return aux

x = 1
_l_(14625)
y = PreIncrement('x') #y and x are both 2
_l_(14626) #y and x are both 2
a = 1
_l_(14627)
b = PostIncrement('a') #b is 1 and a is 2
_l_(14628) #b is 1 and a is 2

x = 1
_l_(14629)
def test():
    _l_(14633)

    x = 10
    _l_(14630)
    y = PreIncrement('x') #y will be 2, local x will be still 10 and global x will be changed to 2
    _l_(14631) #y will be 2, local x will be still 10 and global x will be changed to 2
    z = PreIncrement('x', locals()) #z will be 11, local x will be 11 and global x will be unaltered
    _l_(14632) #z will be 11, local x will be 11 and global x will be unaltered
test()
_l_(14634)

x = 1
_l_(14635)
print(PreIncrement('x'))   #print(x+=1) is illegal!
_l_(14636)   #print(x+=1) is illegal!

x = 1
_l_(14637)
x+=1
_l_(14638)
print(x)
_l_(14639)

def PreDecrement(name, local={}):
    _l_(14645)

    #Equivalent to --name
    if name in local:
        _l_(14642)

        local[name]-=1
        _l_(14640)
        aux = local[name]
        _l_(14641)
        return aux
    globals()[name]-=1
    _l_(14643)
    aux = globals()[name]
    _l_(14644)
    return aux

def PostDecrement(name, local={}):
    _l_(14651)

    #Equivalent to name--
    if name in local:
        _l_(14648)

        local[name]-=1
        _l_(14646)
        aux = local[name]+1
        _l_(14647)
        return aux
    globals()[name]-=1
    _l_(14649)
    aux = globals()[name]+1
    _l_(14650)
    return aux

