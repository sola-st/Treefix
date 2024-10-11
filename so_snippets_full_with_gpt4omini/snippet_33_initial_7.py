'baz' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment
from l3.Runtime import _l_
new_list = old_list.copy()
_l_(2)

new_list = old_list[:]
_l_(3)

new_list = list(old_list)
_l_(4)
try:
    import copy
    _l_(6)

except ImportError:
    pass
new_list = copy.copy(old_list)
_l_(7)
try:
    import copy
    _l_(9)

except ImportError:
    pass
new_list = copy.deepcopy(old_list)
_l_(10)
try:
    import copy
    _l_(12)

except ImportError:
    pass

class Foo(object):
    _l_(17)

    def __init__(self, val):
        _l_(14)

        self.val = val
        _l_(13)

    def __repr__(self):
        _l_(16)

        aux = f'Foo({self.val!r})'
        _l_(15)
        return aux

foo = Foo(1)
_l_(18)

a = ['foo', foo]
_l_(19)
b = a.copy()
_l_(20)
c = a[:]
_l_(21)
d = list(a)
_l_(22)
e = copy.copy(a)
_l_(23)
f = copy.deepcopy(a)
_l_(24)

# edit orignal list and instance 
a.append('baz')
_l_(25)
foo.val = 5
_l_(26)

print(f'original: {a}\nlist.copy(): {b}\nslice: {c}\nlist(): {d}\ncopy: {e}\ndeepcopy: {f}')
_l_(27)

original: ['foo', Foo(5), 'baz']
_l_(28)
# list.copy(): ['foo', Foo(5)]
slice: ['foo', Foo(5)]
_l_(29)
# list(): ['foo', Foo(5)]
copy: ['foo', Foo(5)]
_l_(30)
deepcopy: ['foo', Foo(1)]
_l_(31)

