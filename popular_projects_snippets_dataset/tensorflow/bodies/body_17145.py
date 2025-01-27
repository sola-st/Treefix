# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_shape = [3, 3, 1]

y = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_shape = [4, 3, 1]
x = np.array(x).reshape(x_shape)
y = np.array(y).reshape(y_shape)

i = constant_op.constant([1, 0, 4, 3], dtype=dtypes.int64)
y_tf = image_ops.pad_to_bounding_box_internal(
    x, i[0], i[1], i[2], i[3], check_dims=False)
with self.cached_session():
    self.assertAllClose(y, self.evaluate(y_tf))
