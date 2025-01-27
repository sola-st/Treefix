# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/listdiff_op_test.py
for dtype in [dtypes.int32, dtypes.int64]:
    for index_dtype in [dtypes.int32, dtypes.int64]:
        with self.session():
            x_tensor = ops.convert_to_tensor(x, dtype=dtype)
            y_tensor = ops.convert_to_tensor(y, dtype=dtype)
            with self.test_scope():
                out_tensor, idx_tensor = array_ops.listdiff(
                    x_tensor, y_tensor, out_idx=index_dtype)
                tf_out, tf_idx = self.evaluate([out_tensor, idx_tensor])
        self.assertAllEqual(out, tf_out)
        self.assertAllEqual(idx, tf_idx)
        self.assertEqual(1, out_tensor.get_shape().ndims)
        self.assertEqual(1, idx_tensor.get_shape().ndims)
