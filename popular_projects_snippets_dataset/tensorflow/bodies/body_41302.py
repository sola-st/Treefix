# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
x = constant_op.constant(1, dtype=dtypes.int32)

@polymorphic_function.function
def add_int32s():
    exit(x + x)

self.assertEqual(2, int(add_int32s()))
