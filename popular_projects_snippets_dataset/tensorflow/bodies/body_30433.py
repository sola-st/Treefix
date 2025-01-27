# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
# NOTE(mrry): We cannot currently handle partially-known values,
# because `tf.slice()` uses -1 to specify a wildcard size, and
# this can't be handled using the
# `tensor_util.constant_value_as_shape()` trick.
a = constant_op.constant([[1, 2, 3], [4, 5, 6]])
begin = constant_op.constant(0)
size = constant_op.constant(1)
b = array_ops.slice(a, [begin, 0], [size, 2])
self.assertEqual([1, 2], b.get_shape())

# placeholders only make sense in a graph.
with ops.Graph().as_default():
    a = constant_op.constant([[1, 2, 3], [4, 5, 6]])
    begin = array_ops.placeholder(dtypes.int32, shape=())
    c = array_ops.slice(a, [begin, 0], [-1, 2])
    self.assertEqual([None, 2], c.get_shape().as_list())
