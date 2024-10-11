ClassName = type('ClassName', (object,), {}) # pragma: no cover
ClassName.static_method = staticmethod(lambda kwarg1=None: f'Return value for {kwarg1}') # pragma: no cover
ClassName.class_method = classmethod(lambda cls, kwarg1=None: f'Class method return value for {kwarg1} and class {cls}') # pragma: no cover

class ClassName(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def static_method(kwarg1=None): # pragma: no cover
        return f'Static Method Output with {kwarg1}' # pragma: no cover
    @classmethod # pragma: no cover
    def class_method(cls, kwarg1=None): # pragma: no cover
        return f'Class Method Output with {kwarg1}' # pragma: no cover
ClassName.StaticMethod = ClassName.static_method # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/735975/static-methods-in-python
from l3.Runtime import _l_
ClassName.StaticMethod()
_l_(260)

class ClassName(object):
    _l_(263)


    @staticmethod
    def static_method(kwarg1=None):
        _l_(262)

        '''return a value that is a function of kwarg1'''
        _l_(261)

class ClassName(object):
    _l_(267)


    def static_method(kwarg1=None):
        _l_(265)

        '''return a value that is a function of kwarg1'''
        _l_(264)

    static_method = staticmethod(static_method)
    _l_(266)

ClassName.static_method()
_l_(268)

class ClassName(object):
    _l_(271)


    @classmethod
    def class_method(cls, kwarg1=None):
        _l_(270)

        '''return a value that is a function of the class and kwarg1'''
        _l_(269)

new_instance = ClassName.class_method()
_l_(272)

new_dict = dict.fromkeys(['key1', 'key2'])
_l_(273)

