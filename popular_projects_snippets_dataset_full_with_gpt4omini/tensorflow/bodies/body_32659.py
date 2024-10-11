# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
eye_np = np.eye(num_rows, M=num_columns, dtype=dtype.as_numpy_dtype)
eye_np = np.tile(eye_np, batch_shape + [1, 1])
num_rows_placeholder = array_ops.placeholder(
    dtypes.int32, name="num_rows")
num_columns_placeholder = array_ops.placeholder(
    dtypes.int32, name="num_columns")
batch_shape_placeholder = array_ops.placeholder(
    dtypes.int32, name="batch_shape")
eye = linalg_ops.eye(
    num_rows_placeholder,
    num_columns=num_columns_placeholder,
    batch_shape=batch_shape_placeholder,
    dtype=dtype)
with self.session() as sess:
    eye_tf = sess.run(
        eye,
        feed_dict={
            num_rows_placeholder: num_rows,
            num_columns_placeholder: num_columns,
            batch_shape_placeholder: batch_shape
        })
self.assertAllEqual(eye_np, eye_tf)
