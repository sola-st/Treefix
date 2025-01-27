# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

class OrdinaryClass:
    pass

class OrdinaryCallableClass:

    def __call__(self):
        pass

class Metaclass(type):
    pass

class CallableMetaclass(type):

    def __call__(cls):
        pass

self.assertTrue(inspect_utils.isconstructor(OrdinaryClass))
self.assertTrue(inspect_utils.isconstructor(OrdinaryCallableClass))
self.assertTrue(inspect_utils.isconstructor(Metaclass))
self.assertTrue(inspect_utils.isconstructor(Metaclass('TestClass', (), {})))
self.assertTrue(inspect_utils.isconstructor(CallableMetaclass))

self.assertFalse(inspect_utils.isconstructor(
    CallableMetaclass('TestClass', (), {})))
