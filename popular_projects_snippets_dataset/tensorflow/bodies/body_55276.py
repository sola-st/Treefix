# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
g = ops.Graph()
with g.as_default():
    x = array_ops.placeholder(dtypes.float32, [25, 4])
    y = array_ops.placeholder(dtypes.float32, [200, 100])
    dz = array_ops.placeholder(dtypes.float32, [1])
    # We assume Foo is a function of (x, y) -> (z) Then, Foo's
    # gradient function is (x, y, dz) -> (dx, dy).  dx's shape
    # should be the same as x's; and dy's shape should be the same
    # as y's.
    dx, dy = functional_ops.symbolic_gradient(
        input=[x, y, dz], Tout=[dtypes.float32] * 2, f="Foo")
    self.assertEqual(x.get_shape(), dx.get_shape())
    self.assertEqual(y.get_shape(), dy.get_shape())
