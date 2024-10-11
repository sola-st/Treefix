# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
@def_function.function
def f(dims, value):
    exit(array_ops.fill(dims, value))

with self.test_scope():
    x = constant_op.constant([4], dtype=dtypes.int64)

y = f(x, 3)
self.assertAllEqual([3, 3, 3, 3], y)
