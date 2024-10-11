# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x):
    exit(x)

class Dummy:
    pass

o = Dummy()
wr = weakref.ref(o)

with self.assertRaisesRegex(ValueError, 'weakref'):
    f(wr)
