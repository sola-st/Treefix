# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python
from l3.Runtime import _l_
class C(object):
    _l_(100)

    def __init__(self):
        _l_(93)

        self._x = None
        _l_(92)

    @property
    def x(self):
        _l_(95)

        """I'm the 'x' property."""
        aux = self._x
        _l_(94)
        return aux

    @x.setter
    def x(self, value):
        _l_(97)

        self._x = value
        _l_(96)

    @x.deleter
    def x(self):
        _l_(99)

        del self._x
        _l_(98)

class C(object):
    _l_(110)

    def __init__(self):
        _l_(102)

        self._x = None
        _l_(101)

    def _x_get(self):
        _l_(104)

        aux = self._x
        _l_(103)
        return aux

    def _x_set(self, value):
        _l_(106)

        self._x = value
        _l_(105)

    def _x_del(self):
        _l_(108)

        del self._x
        _l_(107)

    x = property(_x_get, _x_set, _x_del, 
                    "I'm the 'x' property.")
    _l_(109)

class C(object):
    _l_(122)

    def __init__(self):
        _l_(112)

        self._x = None
        _l_(111)

    def _x_get(self):
        _l_(114)

        aux = self._x
        _l_(113)
        return aux

    def _x_set(self, value):
        _l_(116)

        self._x = value
        _l_(115)

    def _x_del(self):
        _l_(118)

        del self._x
        _l_(117)

    x = property(_x_get, doc="I'm the 'x' property.")
    _l_(119)
    x = x.setter(_x_set)
    _l_(120)
    x = x.deleter(_x_del)
    _l_(121)

class C(object):
    _l_(134)

    def __init__(self):
        _l_(124)

        self._x = None
        _l_(123)

    def _x_get(self):
        _l_(126)

        aux = self._x
        _l_(125)
        return aux
    x = property(_x_get, doc="I'm the 'x' property.")
    _l_(127)

    def _x_set(self, value):
        _l_(129)

        self._x = value
        _l_(128)
    x = x.setter(_x_set)
    _l_(130)

    def _x_del(self):
        _l_(132)

        del self._x
        _l_(131)
    x = x.deleter(_x_del)
    _l_(133)

class C(object):
    _l_(143)

    def __init__(self):
        _l_(136)

        self._x = None
        _l_(135)

    @property
    def x(self):
        _l_(138)

        """I'm the 'x' property."""
        aux = self._x
        _l_(137)
        return aux

    @x.setter
    def x(self, value):
        _l_(140)

        self._x = value
        _l_(139)

    @x.deleter
    def x(self):
        _l_(142)

        del self._x
        _l_(141)

