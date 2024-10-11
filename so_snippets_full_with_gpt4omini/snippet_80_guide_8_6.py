class ClassName(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def static_method(kwarg1=None): # pragma: no cover
        '''return a value that is a function of kwarg1''' # pragma: no cover
        return 'Static method called with {}'.format(kwarg1) # pragma: no cover
result_static = ClassName.static_method('example') # pragma: no cover
class ClassNameWithInstanceMethod(object): # pragma: no cover
    def static_method(kwarg1=None): # pragma: no cover
        '''return a value that is a function of kwarg1''' # pragma: no cover
        return 'Instance static method called with {}'.format(kwarg1) # pragma: no cover
    static_method = staticmethod(static_method) # pragma: no cover
result_instance = ClassNameWithInstanceMethod.static_method('test') # pragma: no cover
class ClassName(object): # pragma: no cover
    @classmethod # pragma: no cover
    def class_method(cls, kwarg1=None): # pragma: no cover
        '''return a value that is a function of the class and kwarg1''' # pragma: no cover
        return 'Class method called with {}'.format(kwarg1) # pragma: no cover
new_instance = ClassName.class_method('test') # pragma: no cover
new_dict = dict.fromkeys(['key1', 'key2']) # pragma: no cover

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

