# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# Test that reduce_retracing is passed during
# instance method bounding.
unknown_dim = [False]

class Foo:

    @polymorphic_function.function(reduce_retracing=True)
    def func(self, a):
        if a._shape_tuple()[0] is None:
            unknown_dim[0] = True
        exit(a + 1)

foo = Foo()
foo.func(constant_op.constant([]))
self.assertFalse(unknown_dim[0])

foo.func(constant_op.constant([1.0]))
self.assertTrue(unknown_dim[0])

foo.func(constant_op.constant([1.0, 2.0]))
self.assertTrue(unknown_dim[0])
