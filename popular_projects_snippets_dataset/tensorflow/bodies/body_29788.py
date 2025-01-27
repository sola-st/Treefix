# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
# Unknown multiples shape.
inp = constant_op.constant(0.0, shape=[4, 4, 4, 4])
tiled = array_ops.tile(inp, array_ops.placeholder(dtypes.int32))
self.assertEqual([None, None, None, None], tiled.get_shape().as_list())

# Unknown input shape.
inp = array_ops.placeholder(dtypes.float32)
tiled = array_ops.tile(inp, [2, 2, 2, 2])
self.assertEqual([None, None, None, None], tiled.get_shape().as_list())

# Unknown input and multiples shape.
inp = array_ops.placeholder(dtypes.float32)
tiled = array_ops.tile(inp, array_ops.placeholder(dtypes.int32))
self.assertIs(None, tiled.get_shape().ndims)

# Known input and partially known multiples.
inp = constant_op.constant(0.0, shape=[1, 1])
tiled = array_ops.tile(inp, [array_ops.placeholder(dtypes.int32), 7])
self.assertEqual([None, 7], tiled.get_shape().as_list())

# Mismatched input rank and multiples length.
inp = array_ops.placeholder(dtypes.float32, shape=[None, None])
with self.assertRaises(ValueError):
    tiled = array_ops.tile(
        inp, array_ops.placeholder(
            dtypes.int32, shape=[3]))
