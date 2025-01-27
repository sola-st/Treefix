# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v = [
    variables_lib.Variable([[1, 2], [3, 4], [5, 6]]),
    variables_lib.Variable([[7, 8], [9, 10], [11, 12]]),
    variables_lib.Variable([[13, 14], [15, 16]])
]
sv = sharded_variable.ShardedVariable(v)
empty = v[0][0:0]

# Test cases: positive step
self.assertAllEqual(sv[:], array_ops.concat(v, axis=0))
self.assertAllEqual(sv[:2], [[1, 2], [3, 4]])
self.assertAllEqual(sv[-8:2], [[1, 2], [3, 4]])
self.assertAllEqual(sv[-10:2], [[1, 2], [3, 4]])
self.assertAllEqual(sv[5:], [[11, 12], [13, 14], [15, 16]])
self.assertAllEqual(sv[5:-1], [[11, 12], [13, 14]])
self.assertAllEqual(sv[::3], [[1, 2], [7, 8], [13, 14]])
self.assertAllEqual(sv[::5], [[1, 2], [11, 12]])
self.assertAllEqual(sv[1::6], [[3, 4], [15, 16]])
self.assertAllEqual(sv[1:5:6], [[3, 4]])
self.assertAllEqual(sv[1::7], [[3, 4]])
self.assertAllEqual(sv[2:7], [[5, 6], [7, 8], [9, 10], [11, 12], [13, 14]])
self.assertAllEqual(sv[2:7:2], [[5, 6], [9, 10], [13, 14]])
self.assertAllEqual(sv[2:7:3], [[5, 6], [11, 12]])

# Test cases: negative step
self.assertAllEqual(
    sv[::-1], array_ops.reverse(array_ops.concat(v, axis=0), axis=[0]))
self.assertAllEqual(sv[2::-1], [[5, 6], [3, 4], [1, 2]])
self.assertAllEqual(sv[2:-8:-1], [[5, 6], [3, 4]])
self.assertAllEqual(sv[2:-10:-1], [[5, 6], [3, 4], [1, 2]])
self.assertAllEqual(sv[4::-1], [[9, 10], [7, 8], [5, 6], [3, 4], [1, 2]])
self.assertAllEqual(sv[-1:-3:-1], [[15, 16], [13, 14]])
self.assertAllEqual(sv[::-5], [[15, 16], [5, 6]])
self.assertAllEqual(sv[6::-6], [[13, 14], [1, 2]])
self.assertAllEqual(sv[6:5:-6], [[13, 14]])
self.assertAllEqual(sv[6::-7], [[13, 14]])
self.assertAllEqual(sv[7:1:-1],
                    [[15, 16], [13, 14], [11, 12], [9, 10], [7, 8], [5, 6]])
self.assertAllEqual(sv[7:1:-2], [[15, 16], [11, 12], [7, 8]])
self.assertAllEqual(sv[7:1:-4], [[15, 16], [7, 8]])

# Test cases: empty slice
self.assertAllEqual(sv[0:0], empty)
self.assertAllEqual(sv[5:3], empty)
self.assertAllEqual(sv[3:5:-1], empty)
self.assertAllEqual(sv[-1:0], empty)
self.assertAllEqual(sv[2:-1:-1], empty)

# Test cases: slicing other dimensions
self.assertAllEqual(sv[:, 0], [1, 3, 5, 7, 9, 11, 13, 15])
self.assertAllEqual(sv[:, 0:1], [[1], [3], [5], [7], [9], [11], [13], [15]])

# Test cases: normal indexing
self.assertAllEqual(sv[2], [5, 6])
self.assertAllEqual(sv[6], [13, 14])
self.assertAllEqual(sv[2, 1], 6)
self.assertAllEqual(sv[-2], [13, 14])
with self.assertRaisesRegex(IndexError, 'out of bounds'):
    _ = sv[100]
with self.assertRaisesRegex(IndexError, 'out of bounds'):
    _ = sv[-100]

# Test cases: Ellipsis
self.assertAllEqual(sv[...], array_ops.concat(v, axis=0))
self.assertAllEqual(sv[..., 0], [1, 3, 5, 7, 9, 11, 13, 15])
self.assertAllEqual(sv[0:1, ...], [[1, 2]])

# Test cases: newaxis
self.assertAllEqual(
    sv[array_ops.newaxis, ...],
    array_ops.expand_dims_v2(array_ops.concat(v, axis=0), axis=0))

# Test cases: boolean masks
self.assertAllEqual(sv[ops.convert_to_tensor(sv) > 10],
                    [11, 12, 13, 14, 15, 16])

# Test cases: tensor input
with self.assertRaisesRegex(TypeError, 'not allowed'):
    _ = sv[constant_op.constant(1)::]
with self.assertRaisesRegex(TypeError, 'not allowed'):
    _ = sv[:constant_op.constant(1):]
with self.assertRaisesRegex(TypeError, 'not allowed'):
    _ = sv[constant_op.constant(1)]

# Test cases: inside tf.function
@def_function.function
def func():
    a = sv[:, 0]
    exit(a)

self.assertAllEqual(func(), [1, 3, 5, 7, 9, 11, 13, 15])
