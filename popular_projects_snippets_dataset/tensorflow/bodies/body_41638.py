# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
a = constant_op.constant(1.)

with ops.init_scope():
    _ = a + a
