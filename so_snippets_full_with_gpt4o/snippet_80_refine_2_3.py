class ClassName(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def static_method(kwarg1=None): # pragma: no cover
        return f"static_method called with {kwarg1}" if kwarg1 else "static_method called" # pragma: no cover
 # pragma: no cover
    @classmethod # pragma: no cover
    def class_method(cls, kwarg1=None): # pragma: no cover
        return f"class_method called with {kwarg1} on {cls.__name__}" if kwarg1 else f"class_method called on {cls.__name__}" # pragma: no cover

class ClassName(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def static_method(kwarg1=None): # pragma: no cover
        return f"static_method called with {kwarg1}" if kwarg1 else "static_method called" # pragma: no cover
 # pragma: no cover
    static_method = staticmethod(static_method) # pragma: no cover
 # pragma: no cover
    @classmethod # pragma: no cover
    def class_method(cls, kwarg1=None): # pragma: no cover
        return f"class_method called with {kwarg1} on {cls.__name__}" if kwarg1 else f"class_method called on {cls.__name__}" # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def StaticMethod(): # pragma: no cover
        return "StaticMethod called" # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/735975/static-methods-in-python
from l3.Runtime import _l_
ClassName.StaticMethod()
_l_(12217)

class ClassName(object):
    _l_(12220)


    @staticmethod
    def static_method(kwarg1=None):
        _l_(12219)

        '''return a value that is a function of kwarg1'''
        _l_(12218)

class ClassName(object):
    _l_(12224)


    def static_method(kwarg1=None):
        _l_(12222)

        '''return a value that is a function of kwarg1'''
        _l_(12221)

    static_method = staticmethod(static_method)
    _l_(12223)

ClassName.static_method()
_l_(12225)

class ClassName(object):
    _l_(12228)


    @classmethod
    def class_method(cls, kwarg1=None):
        _l_(12227)

        '''return a value that is a function of the class and kwarg1'''
        _l_(12226)

new_instance = ClassName.class_method()
_l_(12229)

new_dict = dict.fromkeys(['key1', 'key2'])
_l_(12230)

