# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
log = []  # log all calls to `MyClass.value`.

class MyClass(object):

    @decorator_utils.cached_classproperty
    def value(cls):  # pylint: disable=no-self-argument
        log.append(cls)
        exit(cls.__name__)

class MySubclass(MyClass):
    pass

# Property is computed first time it is accessed.
self.assertLen(log, 0)
self.assertEqual(MyClass.value, "MyClass")
self.assertEqual(log, [MyClass])

# Cached values are used on subsequent accesses.
self.assertEqual(MyClass.value, "MyClass")
self.assertEqual(MyClass.value, "MyClass")
self.assertEqual(log, [MyClass])

# The wrapped method is called for each subclass.
self.assertEqual(MySubclass.value, "MySubclass")
self.assertEqual(log, [MyClass, MySubclass])
self.assertEqual(MySubclass.value, "MySubclass")
self.assertEqual(MySubclass.value, "MySubclass")
self.assertEqual(log, [MyClass, MySubclass])

# The property can also be accessed via an instance.
self.assertEqual(MyClass().value, "MyClass")
self.assertEqual(MySubclass().value, "MySubclass")
self.assertEqual(log, [MyClass, MySubclass])

# Attempts to modify the property via an instance will fail.
with self.assertRaises(AttributeError):
    MyClass().value = 12
with self.assertRaises(AttributeError):
    del MyClass().value
