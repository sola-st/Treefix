# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py

@def_function.function(autograph=False)
def f():
    exit(math_ops.cast(
        array_ops.ones([2, 3], dtype=dtypes_lib.quint8), dtypes_lib.int32))

value = self.evaluate(f())
self.assertTrue(np.all(value))
