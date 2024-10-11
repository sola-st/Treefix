# Extracted from https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort
Python 2.7.12 (default, Sep 29 2016, 13:30:34) 
(0,"foo") < ("foo",0)
True  

Python 3.5.2 (default, Oct 14 2016, 12:54:53) 
(0,"foo") < ("foo",0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: unorderable types: int() < str()

d = lambda s: s.lower()+s.swapcase()

import functools
import itertools


@functools.total_ordering
class NaturalStringA(str):
    def __repr__(self):
        return "{}({})".format\
            ( type(self).__name__
            , super().__repr__()
            )
    d = lambda c, s: [ c.NaturalStringPart("".join(v))
                        for k,v in
                       itertools.groupby(s, c.isdigit)
                     ]
    d = classmethod(d)
    @functools.total_ordering
    class NaturalStringPart(str):
        d = lambda s: "".join(c.lower()+c.swapcase() for c in s)
        d = staticmethod(d)
        def __lt__(self, other):
            if not isinstance(self, type(other)):
                return NotImplemented
            try:
                return int(self) < int(other)
            except ValueError:
                if self.isdigit():
                    return True
                elif other.isdigit():
                    return False
                else:
                    return self.d(self) < self.d(other)
        def __eq__(self, other):
            if not isinstance(self, type(other)):
                return NotImplemented
            try:
                return int(self) == int(other)
            except ValueError:
                if self.isdigit() or other.isdigit():
                    return False
                else:
                    return self.d(self) == self.d(other)
        __le__ = object.__le__
        __ne__ = object.__ne__
        __gt__ = object.__gt__
        __ge__ = object.__ge__
    def __lt__(self, other):
        return self.d(self) < self.d(other)
    def __eq__(self, other):
        return self.d(self) == self.d(other)
    __le__ = object.__le__
    __ne__ = object.__ne__
    __gt__ = object.__gt__
    __ge__ = object.__ge__

import functools
import itertools


@functools.total_ordering
class NaturalStringB(str):
    def __repr__(self):
        return "{}({})".format\
            ( type(self).__name__
            , super().__repr__()
            )
    d = lambda s: "".join(c.lower()+c.swapcase() for c in s)
    d = staticmethod(d)
    def __lt__(self, other):
        if not isinstance(self, type(other)):
            return NotImplemented
        groups = map(lambda i: itertools.groupby(i, type(self).isdigit), (self, other))
        zipped = itertools.zip_longest(*groups)
        for s,o in zipped:
            if s is None:
                return True
            if o is None:
                return False
            s_k, s_v = s[0], "".join(s[1])
            o_k, o_v = o[0], "".join(o[1])
            if s_k and o_k:
                s_v, o_v = int(s_v), int(o_v)
                if s_v == o_v:
                    continue
                return s_v < o_v
            elif s_k:
                return True
            elif o_k:
                return False
            else:
                s_v, o_v = self.d(s_v), self.d(o_v)
                if s_v == o_v:
                    continue
                return s_v < o_v
        return False
    def __eq__(self, other):
        if not isinstance(self, type(other)):
            return NotImplemented
        groups = map(lambda i: itertools.groupby(i, type(self).isdigit), (self, other))
        zipped = itertools.zip_longest(*groups)
        for s,o in zipped:
            if s is None or o is None:
                return False
            s_k, s_v = s[0], "".join(s[1])
            o_k, o_v = o[0], "".join(o[1])
            if s_k and o_k:
                s_v, o_v = int(s_v), int(o_v)
                if s_v == o_v:
                    continue
                return False
            elif s_k or o_k:
                return False
            else:
                s_v, o_v = self.d(s_v), self.d(o_v)
                if s_v == o_v:
                    continue
                return False
        return True
    __le__ = object.__le__
    __ne__ = object.__ne__
    __gt__ = object.__gt__
    __ge__ = object.__ge__

import functools
import itertools
import enum


class OrderingType(enum.Enum):
    PerWordSwapCase         = lambda s: s.lower()+s.swapcase()
    PerCharacterSwapCase    = lambda s: "".join(c.lower()+c.swapcase() for c in s)


class NaturalOrdering:
    @classmethod
    def by(cls, ordering):
        def wrapper(string):
            return cls(string, ordering)
        return wrapper
    def __init__(self, string, ordering=OrderingType.PerCharacterSwapCase):
        self.string = string
        self.groups = [ (k,int("".join(v)))
                            if k else
                        (k,ordering("".join(v)))
                            for k,v in
                        itertools.groupby(string, str.isdigit)
                      ]
    def __repr__(self):
        return "{}({})".format\
            ( type(self).__name__
            , self.string
            )
    def __lesser(self, other, default):
        if not isinstance(self, type(other)):
            return NotImplemented
        for s,o in itertools.zip_longest(self.groups, other.groups):
            if s is None:
                return True
            if o is None:
                return False
            s_k, s_v = s
            o_k, o_v = o
            if s_k and o_k:
                if s_v == o_v:
                    continue
                return s_v < o_v
            elif s_k:
                return True
            elif o_k:
                return False
            else:
                if s_v == o_v:
                    continue
                return s_v < o_v
        return default
    def __lt__(self, other):
        return self.__lesser(other, default=False)
    def __le__(self, other):
        return self.__lesser(other, default=True)
    def __eq__(self, other):
        if not isinstance(self, type(other)):
            return NotImplemented
        for s,o in itertools.zip_longest(self.groups, other.groups):
            if s is None or o is None:
                return False
            s_k, s_v = s
            o_k, o_v = o
            if s_k and o_k:
                if s_v == o_v:
                    continue
                return False
            elif s_k or o_k:
                return False
            else:
                if s_v == o_v:
                    continue
                return False
        return True
    # functools.total_ordering doesn't create single-call wrappers if both
    # __le__ and __lt__ exist, so do it manually.
    def __gt__(self, other):
        op_result = self.__le__(other)
        if op_result is NotImplemented:
            return op_result
        return not op_result
    def __ge__(self, other):
        op_result = self.__lt__(other)
        if op_result is NotImplemented:
            return op_result
        return not op_result
    # __ne__ is the only implied ordering relationship, it automatically
    # delegates to __eq__

import natsort
import timeit
l1 = ['Apple', 'corn', 'apPlE', 'arbour', 'Corn', 'Banana', 'apple', 'banana']
l2 = list(map(str, range(30)))
l3 = ["{} {}".format(x,y) for x in l1 for y in l2]
print(timeit.timeit('sorted(l3+["0"], key=NaturalStringA)', number=10000, globals=globals()))
362.4729259099986
print(timeit.timeit('sorted(l3+["0"], key=NaturalStringB)', number=10000, globals=globals()))
189.7340817489967
print(timeit.timeit('sorted(l3+["0"], key=NaturalOrdering.by(OrderingType.PerCharacterSwapCase))', number=10000, globals=globals()))
69.34636392899847
print(timeit.timeit('natsort.natsorted(l3+["0"], alg=natsort.ns.GROUPLETTERS | natsort.ns.LOWERCASEFIRST)', number=10000, globals=globals()))
98.2531585780016

