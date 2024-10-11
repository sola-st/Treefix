# Extracted from https://stackoverflow.com/questions/68645/class-static-variables-and-methods
class Test(object):

    # regular instance method:
    def my_method(self):
        pass

    # class method:
    @classmethod
    def my_class_method(cls):
        pass

    # static method:
    @staticmethod
    def my_static_method():
        pass

class Test(object):
    i = 3  # This is a class attribute

x = Test()
x.i = 12   # Attempt to change the value of the class attribute using x instance
assert x.i == Test.i  # ERROR
assert Test.i == 3    # Test.i was not affected
assert x.i == 12      # x.i is a different object than Test.i

class Test(object):

    _i = 3

    @property
    def i(self):
        return type(self)._i

    @i.setter
    def i(self,val):
        type(self)._i = val

## ALTERNATIVE IMPLEMENTATION - FUNCTIONALLY EQUIVALENT TO ABOVE ##
## (except with separate methods for getting and setting i) ##

class Test(object):

    _i = 3

    def get_i(self):
        return type(self)._i

    def set_i(self,val):
        type(self)._i = val

    i = property(get_i, set_i)

x1 = Test()
x2 = Test()
x1.i = 50
assert x2.i == x1.i  # no error
assert x2.i == 50    # the property is synced

class Test(object):

    _i = 3

    @property
    def i(self):
        return type(self)._i

## ALTERNATIVE IMPLEMENTATION - FUNCTIONALLY EQUIVALENT TO ABOVE ##
## (except with separate methods for getting i) ##

class Test(object):

    _i = 3

    def get_i(self):
        return type(self)._i

    i = property(get_i)

x = Test()
assert x.i == 3  # success
x.i = 12         # ERROR

x = Test()
assert x.i == Test.i  # ERROR

# x.i and Test.i are two different objects:
type(Test.i)  # class 'property'
type(x.i)     # class 'int'

    i = property(get_i) 

type(int)  # class 'type'
type(str)  # class 'type'
class Test(): pass
type(Test) # class 'type'

class MyMeta(type): pass

class MyClass(metaclass = MyMeta):
    pass

type(MyClass)  # class MyMeta

from functools import wraps

class StaticVarsMeta(type):
    '''A metaclass for creating classes that emulate the "static variable" behavior
    of other languages. I do not advise actually using this for anything!!!
    
    Behavior is intended to be similar to classes that use __slots__. However, "normal"
    attributes and __statics___ can coexist (unlike with __slots__). 
    
    Example usage: 
        
        class MyBaseClass(metaclass = StaticVarsMeta):
            __statics__ = {'a','b','c'}
            i = 0  # regular attribute
            a = 1  # static var defined (optional)
            
        class MyParentClass(MyBaseClass):
            __statics__ = {'d','e','f'}
            j = 2              # regular attribute
            d, e, f = 3, 4, 5  # Static vars
            a, b, c = 6, 7, 8  # Static vars (inherited from MyBaseClass, defined/re-defined here)
            
        class MyChildClass(MyParentClass):
            __statics__ = {'a','b','c'}
            j = 2  # regular attribute (redefines j from MyParentClass)
            d, e, f = 9, 10, 11   # Static vars (inherited from MyParentClass, redefined here)
            a, b, c = 12, 13, 14  # Static vars (overriding previous definition in MyParentClass here)'''
    statics = {}
    def __new__(mcls, name, bases, namespace):
        # Get the class object
        cls = super().__new__(mcls, name, bases, namespace)
        # Establish the "statics resolution order"
        cls.__sro__ = tuple(c for c in cls.__mro__ if isinstance(c,mcls))
                        
        # Replace class getter, setter, and deleter for instance attributes
        cls.__getattribute__ = StaticVarsMeta.__inst_getattribute__(cls, cls.__getattribute__)
        cls.__setattr__ = StaticVarsMeta.__inst_setattr__(cls, cls.__setattr__)
        cls.__delattr__ = StaticVarsMeta.__inst_delattr__(cls, cls.__delattr__)
        # Store the list of static variables for the class object
        # This list is permanent and cannot be changed, similar to __slots__
        try:
            mcls.statics[cls] = getattr(cls,'__statics__')
        except AttributeError:
            mcls.statics[cls] = namespace['__statics__'] = set() # No static vars provided
        # Check and make sure the statics var names are strings
        if any(not isinstance(static,str) for static in mcls.statics[cls]):
            typ = dict(zip((not isinstance(static,str) for static in mcls.statics[cls]), map(type,mcls.statics[cls])))[True].__name__
            raise TypeError('__statics__ items must be strings, not {0}'.format(typ))
        # Move any previously existing, not overridden statics to the static var parent class(es)
        if len(cls.__sro__) > 1:
            for attr,value in namespace.items():
                if attr not in StaticVarsMeta.statics[cls] and attr != ['__statics__']:
                    for c in cls.__sro__[1:]:
                        if attr in StaticVarsMeta.statics[c]:
                            setattr(c,attr,value)
                            delattr(cls,attr)
        return cls
    def __inst_getattribute__(self, orig_getattribute):
        '''Replaces the class __getattribute__'''
        @wraps(orig_getattribute)
        def wrapper(self, attr):
            if StaticVarsMeta.is_static(type(self),attr):
                return StaticVarsMeta.__getstatic__(type(self),attr)
            else:
                return orig_getattribute(self, attr)
        return wrapper
    def __inst_setattr__(self, orig_setattribute):
        '''Replaces the class __setattr__'''
        @wraps(orig_setattribute)
        def wrapper(self, attr, value):
            if StaticVarsMeta.is_static(type(self),attr):
                StaticVarsMeta.__setstatic__(type(self),attr, value)
            else:
                orig_setattribute(self, attr, value)
        return wrapper
    def __inst_delattr__(self, orig_delattribute):
        '''Replaces the class __delattr__'''
        @wraps(orig_delattribute)
        def wrapper(self, attr):
            if StaticVarsMeta.is_static(type(self),attr):
                StaticVarsMeta.__delstatic__(type(self),attr)
            else:
                orig_delattribute(self, attr)
        return wrapper
    def __getstatic__(cls,attr):
        '''Static variable getter'''
        for c in cls.__sro__:
            if attr in StaticVarsMeta.statics[c]:
                try:
                    return getattr(c,attr)
                except AttributeError:
                    pass
        raise AttributeError(cls.__name__ + " object has no attribute '{0}'".format(attr))
    def __setstatic__(cls,attr,value):
        '''Static variable setter'''
        for c in cls.__sro__:
            if attr in StaticVarsMeta.statics[c]:
                setattr(c,attr,value)
                break
    def __delstatic__(cls,attr):
        '''Static variable deleter'''
        for c in cls.__sro__:
            if attr in StaticVarsMeta.statics[c]:
                try:
                    delattr(c,attr)
                    break
                except AttributeError:
                    pass
        raise AttributeError(cls.__name__ + " object has no attribute '{0}'".format(attr))
    def __delattr__(cls,attr):
        '''Prevent __sro__ attribute from deletion'''
        if attr == '__sro__':
            raise AttributeError('readonly attribute')
        super().__delattr__(attr)
    def is_static(cls,attr):
        '''Returns True if an attribute is a static variable of any class in the __sro__'''
        if any(attr in StaticVarsMeta.statics[c] for c in cls.__sro__):
            return True
        return False

