# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops_test.py
# Create a tensor with an unknown dim 1.
x = random_ops.random_normal([4, 10, 10])
x = array_ops.gather(
    x,
    array_ops.reshape(array_ops.where_v2(x[0, :, 0] > 0.5), [-1]),
    axis=1)
x.shape.assert_is_compatible_with([4, None, 10])
a = array_ops.reshape(x, array_ops.shape(x))
a.shape.assert_is_compatible_with([4, None, 10])
b = array_ops.reshape(x, math_ops.cast(array_ops.shape(x), dtypes.int64))
b.shape.assert_is_compatible_with([4, None, 10])

# We do not shape-infer across a tf.cast into anything that's not tf.int32
# or tf.int64, since they might end up mangling the shape.
c = array_ops.reshape(
    x,
    math_ops.cast(
        math_ops.cast(array_ops.shape(x), dtypes.float32), dtypes.int32))
c.shape.assert_is_compatible_with([None, None, None])
