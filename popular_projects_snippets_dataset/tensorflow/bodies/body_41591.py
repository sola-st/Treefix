# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
self.assertAllClose(
    3.,
    polymorphic_function.function(
        functools.partial(lambda x, y: x + y,
                          1.))(constant_op.constant(2.)))
