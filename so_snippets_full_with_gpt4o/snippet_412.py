# Extracted from https://stackoverflow.com/questions/674304/why-is-init-always-called-after-new
def SingletonClass(cls):
    class Single(cls):
        __doc__ = cls.__doc__
        _initialized = False
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Single, cls).__new__(cls, *args, **kwargs)
            return cls._instance

        def __init__(self, *args, **kwargs):
            if self._initialized:
                return
            super(Single, self).__init__(*args, **kwargs)
            self.__class__._initialized = True  # Its crucial to set this variable on the class!
    return Single

class Singleton(object):
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls.__initialized:
            cls.__init__(*args, **kwargs)
            cls.__initialized = True
        return cls


class MyClass(Singleton):
    @classmethod
    def __init__(cls, x, y):
        print "init is here"

    @classmethod
    def do(cls):
        print "doing stuff"

