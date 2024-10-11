baz = 'baz' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment
from l3.Runtime import _l_
new_list = old_list.copy()
_l_(11840)

new_list = old_list[:]
_l_(11841)

new_list = list(old_list)
_l_(11842)
try:
    import copy
    _l_(11844)

except ImportError:
    pass
new_list = copy.copy(old_list)
_l_(11845)
try:
    import copy
    _l_(11847)

except ImportError:
    pass
new_list = copy.deepcopy(old_list)
_l_(11848)
try:
    import copy
    _l_(11850)

except ImportError:
    pass

class Foo(object):
    _l_(11855)

    def __init__(self, val):
        _l_(11852)

        self.val = val
        _l_(11851)

    def __repr__(self):
        _l_(11854)

        aux = f'Foo({self.val!r})'
        _l_(11853)
        return aux

foo = Foo(1)
_l_(11856)

a = ['foo', foo]
_l_(11857)
b = a.copy()
_l_(11858)
c = a[:]
_l_(11859)
d = list(a)
_l_(11860)
e = copy.copy(a)
_l_(11861)
f = copy.deepcopy(a)
_l_(11862)

# edit orignal list and instance 
a.append('baz')
_l_(11863)
foo.val = 5
_l_(11864)

print(f'original: {a}\nlist.copy(): {b}\nslice: {c}\nlist(): {d}\ncopy: {e}\ndeepcopy: {f}')
_l_(11865)

original: ['foo', Foo(5), 'baz']
_l_(11866)
# list.copy(): ['foo', Foo(5)]
slice: ['foo', Foo(5)]
_l_(11867)
# list(): ['foo', Foo(5)]
copy: ['foo', Foo(5)]
_l_(11868)
deepcopy: ['foo', Foo(1)]
_l_(11869)

