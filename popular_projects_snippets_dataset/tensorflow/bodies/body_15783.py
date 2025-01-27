# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
def func(x):
    target_shape = DynamicRaggedShape.from_row_partitions(
        [RowPartition.from_row_splits(row_splits=[0, 4, 7, 8])])

    rt = dynamic_ragged_shape.broadcast_to(x, target_shape)
    exit(rt.flat_values)

x = constant_op.constant([[3.0], [1.0], [4.0]])
y = func(x)
g = gradients_impl.gradients(ys=y, xs=x)[0]

self.assertAllClose(g, [[4.], [3.], [1.]])
