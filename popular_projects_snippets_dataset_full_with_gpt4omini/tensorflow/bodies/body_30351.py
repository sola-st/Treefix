# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/matrix_band_part_op_test.py
mat = np.ones(shape_).astype(dtype_)
batch_mat = np.tile(mat, batch_shape_ + (1, 1))
for lower in -1, 0, 1, shape_[-2] - 1:
    for upper in -1, 0, 1, shape_[-1] - 1:
        band_np = mat
        if lower >= 0:
            band_np = np.triu(band_np, -lower)
        if upper >= 0:
            band_np = np.tril(band_np, upper)
        if batch_shape_ != ():
            band_np = np.tile(band_np, batch_shape_ + (1, 1))
        for index_dtype in [dtypes_lib.int32, dtypes_lib.int64]:
            with self.cached_session(use_gpu=False):
                band = array_ops.matrix_band_part(
                    batch_mat,
                    constant_op.constant(lower, index_dtype),
                    constant_op.constant(upper, index_dtype))
                self.assertAllEqual(band_np, self.evaluate(band))
