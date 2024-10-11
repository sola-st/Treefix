# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/listdiff_op_test.py
for dtype in _TYPES:
    if dtype == dtypes.string:
        x = [compat.as_bytes(str(a)) for a in x]
        y = [compat.as_bytes(str(a)) for a in y]
        out = [compat.as_bytes(str(a)) for a in out]
    for diff_func in [array_ops.setdiff1d]:
        for index_dtype in [dtypes.int32, dtypes.int64]:
            with self.cached_session() as sess:
                x_tensor = ops.convert_to_tensor(x, dtype=dtype)
                y_tensor = ops.convert_to_tensor(y, dtype=dtype)
                out_tensor, idx_tensor = diff_func(x_tensor, y_tensor,
                                                   index_dtype=index_dtype)
                tf_out, tf_idx = self.evaluate([out_tensor, idx_tensor])
            self.assertAllEqual(tf_out, out)
            self.assertAllEqual(tf_idx, idx)
            self.assertEqual(1, out_tensor.get_shape().ndims)
            self.assertEqual(1, idx_tensor.get_shape().ndims)
