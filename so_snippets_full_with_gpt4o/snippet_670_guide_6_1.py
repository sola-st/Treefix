from __future__ import division # pragma: no cover
from builtins import range as xrange # pragma: no cover

xrange_object = xrange(2, 10) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/135041/should-you-always-favor-xrange-over-range
from __future__ import division
from l3.Runtime import _l_
_l_(14466)

def read_xrange(xrange_object):
    _l_(14473)

    # returns the xrange object's start, stop, and step
    start = xrange_object[0]
    _l_(14467)
    if len(xrange_object) > 1:
        _l_(14470)

        step = xrange_object[1] - xrange_object[0]
        _l_(14468)
    else:
        step = 1
        _l_(14469)
    stop = xrange_object[-1] + step
    _l_(14471)
    aux = start, stop, step
    _l_(14472)
    return aux

class Xrange(object):
    _l_(14529)

    ''' creates an xrange-like object that supports slicing and indexing.
    ex: a = Xrange(20)
    a.index(10)
    will work

    Also a[:5]
    will return another Xrange object with the specified attributes

    Also allows for the conversion from an existing xrange object
    '''
    _l_(14474)
    def __init__(self, *inputs):
        _l_(14490)

        # allow inputs of xrange objects
        if len(inputs) == 1:
            _l_(14480)

            test, = inputs
            _l_(14475)
            if type(test) == xrange:
                _l_(14479)

                self.xrange = test
                _l_(14476)
                self.start, self.stop, self.step = read_xrange(test)
                _l_(14477)
                aux = ""
                _l_(14478)
                return aux

        # or create one from start, stop, step
        self.start, self.step = 0, None
        _l_(14481)
        if len(inputs) == 1:
            _l_(14488)

            self.stop, = inputs
            _l_(14482)
        elif len(inputs) == 2:
            _l_(14487)

            self.start, self.stop = inputs
            _l_(14483)
        elif len(inputs) == 3:
            _l_(14486)

            self.start, self.stop, self.step = inputs
            _l_(14484)
        else:
            raise ValueError(inputs)
            _l_(14485)

        self.xrange = xrange(self.start, self.stop, self.step)
        _l_(14489)

    def __iter__(self):
        _l_(14492)

        aux = iter(self.xrange)
        _l_(14491)
        return aux

    def __getitem__(self, item):
        _l_(14515)

        if type(item) is int:
            _l_(14496)

            if item < 0:
                _l_(14494)

                item += len(self)
                _l_(14493)
            aux = self.xrange[item]
            _l_(14495)

            return aux

        if type(item) is slice:
            _l_(14514)

            # get the indexes, and then convert to the number
            start, stop, step = item.start, item.stop, item.step
            _l_(14497)
            start = start if start != None else 0 # convert start = None to start = 0
            _l_(14498) # convert start = None to start = 0
            if start < 0:
                _l_(14500)

                start += start
                _l_(14499)
            start = self[start]
            _l_(14501)
            if start < 0:
                _l_(14502)

raise IndexError(item)            step = (self.step if self.step != None else 1) * (step if step != None else 1)
            _l_(14503)
            stop = stop if stop is not None else self.xrange[-1]
            _l_(14504)
            if stop < 0:
                _l_(14506)

                stop += stop
                _l_(14505)

            stop = self[stop]
            _l_(14507)
            stop = stop
            _l_(14508)

            if stop > self.stop:
                _l_(14510)

                raise IndexError
                _l_(14509)
            if start < self.start:
                _l_(14512)

                raise IndexError
                _l_(14511)
            aux = Xrange(start, stop, step)
            _l_(14513)
            return aux

    def index(self, value):
        _l_(14526)

        error = ValueError('object.index({0}): {0} not in object'.format(value))
        _l_(14516)
        index = (value - self.start)/self.step
        _l_(14517)
        if index % 1 != 0:
            _l_(14519)

            raise error
            _l_(14518)
        index = int(index)
        _l_(14520)


        try:
            _l_(14524)

            self.xrange[index]
            _l_(14521)
        except (IndexError, TypeError):
            _l_(14523)

            raise error
            _l_(14522)
        aux = index
        _l_(14525)
        return aux

    def __len__(self):
        _l_(14528)

        aux = len(self.xrange)
        _l_(14527)
        return aux

