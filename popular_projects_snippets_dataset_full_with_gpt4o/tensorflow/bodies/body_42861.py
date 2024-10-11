# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
class MyModule:

    def f(self, a):
        pass

    def __call__(self):
        pass

module = MyModule()
self.assertTrue(tf_inspect.isanytargetmethod(module))
f = module.f
self.assertTrue(tf_inspect.isanytargetmethod(f))
f = functools.partial(f, 1)
self.assertTrue(tf_inspect.isanytargetmethod(f))
f = test_decorator('tf_decorator1')(f)
self.assertTrue(tf_inspect.isanytargetmethod(f))
f = test_decorator('tf_decorator2')(f)
self.assertTrue(tf_inspect.isanytargetmethod(f))

class MyModule2:
    pass
module = MyModule2()
self.assertFalse(tf_inspect.isanytargetmethod(module))
def f2(x):
    del x
self.assertFalse(tf_inspect.isanytargetmethod(f2))
f2 = functools.partial(f2, 1)
self.assertFalse(tf_inspect.isanytargetmethod(f2))
f2 = test_decorator('tf_decorator1')(f2)
self.assertFalse(tf_inspect.isanytargetmethod(f2))
f2 = test_decorator('tf_decorator2')(f2)
self.assertFalse(tf_inspect.isanytargetmethod(f2))
self.assertFalse(tf_inspect.isanytargetmethod(lambda: None))
self.assertFalse(tf_inspect.isanytargetmethod(None))
self.assertFalse(tf_inspect.isanytargetmethod(1))
