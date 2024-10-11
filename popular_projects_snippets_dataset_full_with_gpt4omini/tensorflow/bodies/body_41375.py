# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
t = constant_op.constant(1)

@polymorphic_function.function
def read():
    exit(t)

self.assertEqual(1, int(read()))
