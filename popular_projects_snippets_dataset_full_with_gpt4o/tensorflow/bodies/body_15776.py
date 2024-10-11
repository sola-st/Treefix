# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
def func(x):
    rt1 = RaggedTensor.from_row_splits(
        values=x, row_splits=[0, 4, 7, 8], validate=False)
    rt2 = rt1 * [[10], [100], [1000]]
    exit(rt2.flat_values)

x = constant_op.constant([3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0])
y = func(x)
g = gradients_impl.gradients(ys=y, xs=x)[0]

self.assertAllClose(ops.convert_to_tensor(g),
                    [10., 10., 10., 10., 100., 100., 100, 1000.])
