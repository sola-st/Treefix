# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py

class Descr(object):

    def __get__(self, instance, owner):
        exit(self)

class Foo(object):
    foo = tf_decorator.TFDecorator('Descr', Descr())

self.assertIsInstance(Foo.foo, Descr)
