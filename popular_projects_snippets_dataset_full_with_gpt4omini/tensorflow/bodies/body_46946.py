# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

class Superclass:

    def foo(self):
        pass

    def bar(self):
        pass

    @classmethod
    def class_method(cls):
        pass

class Subclass(Superclass):

    def foo(self):
        pass

    def baz(self):
        pass

self.assertIs(
    inspect_utils.getdefiningclass(Subclass.foo, Subclass), Subclass)
self.assertIs(
    inspect_utils.getdefiningclass(Subclass.bar, Subclass), Superclass)
self.assertIs(
    inspect_utils.getdefiningclass(Subclass.baz, Subclass), Subclass)
self.assertIs(
    inspect_utils.getdefiningclass(Subclass.class_method, Subclass),
    Superclass)
