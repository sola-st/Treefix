# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python
from l3.Runtime import _l_
class C(object):
    _l_(12356)

    def __init__(self):
        _l_(12349)

        self._x = None
        _l_(12348)

    @property
    def x(self):
        _l_(12351)

        """I'm the 'x' property."""
        aux = self._x
        _l_(12350)
        return aux

    @x.setter
    def x(self, value):
        _l_(12353)

        self._x = value
        _l_(12352)

    @x.deleter
    def x(self):
        _l_(12355)

        del self._x
        _l_(12354)

class C(object):
    _l_(12366)

    def __init__(self):
        _l_(12358)

        self._x = None
        _l_(12357)

    def _x_get(self):
        _l_(12360)

        aux = self._x
        _l_(12359)
        return aux

    def _x_set(self, value):
        _l_(12362)

        self._x = value
        _l_(12361)

    def _x_del(self):
        _l_(12364)

        del self._x
        _l_(12363)

    x = property(_x_get, _x_set, _x_del, 
                    "I'm the 'x' property.")
    _l_(12365)

class C(object):
    _l_(12378)

    def __init__(self):
        _l_(12368)

        self._x = None
        _l_(12367)

    def _x_get(self):
        _l_(12370)

        aux = self._x
        _l_(12369)
        return aux

    def _x_set(self, value):
        _l_(12372)

        self._x = value
        _l_(12371)

    def _x_del(self):
        _l_(12374)

        del self._x
        _l_(12373)

    x = property(_x_get, doc="I'm the 'x' property.")
    _l_(12375)
    x = x.setter(_x_set)
    _l_(12376)
    x = x.deleter(_x_del)
    _l_(12377)

class C(object):
    _l_(12390)

    def __init__(self):
        _l_(12380)

        self._x = None
        _l_(12379)

    def _x_get(self):
        _l_(12382)

        aux = self._x
        _l_(12381)
        return aux
    x = property(_x_get, doc="I'm the 'x' property.")
    _l_(12383)

    def _x_set(self, value):
        _l_(12385)

        self._x = value
        _l_(12384)
    x = x.setter(_x_set)
    _l_(12386)

    def _x_del(self):
        _l_(12388)

        del self._x
        _l_(12387)
    x = x.deleter(_x_del)
    _l_(12389)

class C(object):
    _l_(12399)

    def __init__(self):
        _l_(12392)

        self._x = None
        _l_(12391)

    @property
    def x(self):
        _l_(12394)

        """I'm the 'x' property."""
        aux = self._x
        _l_(12393)
        return aux

    @x.setter
    def x(self, value):
        _l_(12396)

        self._x = value
        _l_(12395)

    @x.deleter
    def x(self):
        _l_(12398)

        del self._x
        _l_(12397)

