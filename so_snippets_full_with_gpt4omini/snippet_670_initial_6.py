from __future__ import division # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/135041/should-you-always-favor-xrange-over-range
from __future__ import division
from l3.Runtime import _l_
_l_(2693)

def read_xrange(xrange_object):
    _l_(2700)

    # returns the xrange object's start, stop, and step
    start = xrange_object[0]
    _l_(2694)
    if len(xrange_object) > 1:
        _l_(2697)

        step = xrange_object[1] - xrange_object[0]
        _l_(2695)
    else:
        step = 1
        _l_(2696)
    stop = xrange_object[-1] + step
    _l_(2698)
    aux = start, stop, step
    _l_(2699)
    return aux

class Xrange(object):
    _l_(2756)

    ''' creates an xrange-like object that supports slicing and indexing.
    ex: a = Xrange(20)
    a.index(10)
    will work

    Also a[:5]
    will return another Xrange object with the specified attributes

    Also allows for the conversion from an existing xrange object
    '''
    _l_(2701)
    def __init__(self, *inputs):
        _l_(2717)

        # allow inputs of xrange objects
        if len(inputs) == 1:
            _l_(2707)

            test, = inputs
            _l_(2702)
            if type(test) == xrange:
                _l_(2706)

                self.xrange = test
                _l_(2703)
                self.start, self.stop, self.step = read_xrange(test)
                _l_(2704)
                aux = ""
                _l_(2705)
                return aux

        # or create one from start, stop, step
        self.start, self.step = 0, None
        _l_(2708)
        if len(inputs) == 1:
            _l_(2715)

            self.stop, = inputs
            _l_(2709)
        elif len(inputs) == 2:
            _l_(2714)

            self.start, self.stop = inputs
            _l_(2710)
        elif len(inputs) == 3:
            _l_(2713)

            self.start, self.stop, self.step = inputs
            _l_(2711)
        else:
            raise ValueError(inputs)
            _l_(2712)

        self.xrange = xrange(self.start, self.stop, self.step)
        _l_(2716)

    def __iter__(self):
        _l_(2719)

        aux = iter(self.xrange)
        _l_(2718)
        return aux

    def __getitem__(self, item):
        _l_(2742)

        if type(item) is int:
            _l_(2723)

            if item < 0:
                _l_(2721)

                item += len(self)
                _l_(2720)
            aux = self.xrange[item]
            _l_(2722)

            return aux

        if type(item) is slice:
            _l_(2741)

            # get the indexes, and then convert to the number
            start, stop, step = item.start, item.stop, item.step
            _l_(2724)
            start = start if start != None else 0 # convert start = None to start = 0
            _l_(2725) # convert start = None to start = 0
            if start < 0:
                _l_(2727)

                start += start
                _l_(2726)
            start = self[start]
            _l_(2728)
            if start < 0:
                _l_(2729)

raise IndexError(item)            step = (self.step if self.step != None else 1) * (step if step != None else 1)
            _l_(2730)
            stop = stop if stop is not None else self.xrange[-1]
            _l_(2731)
            if stop < 0:
                _l_(2733)

                stop += stop
                _l_(2732)

            stop = self[stop]
            _l_(2734)
            stop = stop
            _l_(2735)

            if stop > self.stop:
                _l_(2737)

                raise IndexError
                _l_(2736)
            if start < self.start:
                _l_(2739)

                raise IndexError
                _l_(2738)
            aux = Xrange(start, stop, step)
            _l_(2740)
            return aux

    def index(self, value):
        _l_(2753)

        error = ValueError('object.index({0}): {0} not in object'.format(value))
        _l_(2743)
        index = (value - self.start)/self.step
        _l_(2744)
        if index % 1 != 0:
            _l_(2746)

            raise error
            _l_(2745)
        index = int(index)
        _l_(2747)


        try:
            _l_(2751)

            self.xrange[index]
            _l_(2748)
        except (IndexError, TypeError):
            _l_(2750)

            raise error
            _l_(2749)
        aux = index
        _l_(2752)
        return aux

    def __len__(self):
        _l_(2755)

        aux = len(self.xrange)
        _l_(2754)
        return aux

