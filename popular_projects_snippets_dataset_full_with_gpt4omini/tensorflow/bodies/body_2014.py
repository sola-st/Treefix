# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_band_part_test.py
# TODO(b/125505881): Disabled due to LLVM backend crash.
if self.device == 'XLA_CPU' and cols == 7 and rows == 1 and batch_shape == [
    1, 3, 2
]:
    pass
for dtype in self.float_types:
    with self.session():
        mat = np.ones(batch_shape + [rows, cols]).astype(dtype)
        batch_mat = np.tile(mat, batch_shape + [1, 1])
        for lower in -1, 0, 1, rows - 1:
            for upper in -1, 0, 1, cols - 1:
                band_np = mat
                if lower >= 0:
                    band_np = np.triu(band_np, -lower)
                if upper >= 0:
                    band_np = np.tril(band_np, upper)
                if batch_shape:
                    band_np = np.tile(band_np, batch_shape + [1, 1])

                placeholder = array_ops.placeholder(dtype)
                with self.test_scope():
                    band = array_ops.matrix_band_part(
                        placeholder, constant_op.constant(lower, dtype=dtypes.int32),
                        constant_op.constant(upper, dtype=dtypes.int32))
                    feed_dict = {placeholder: batch_mat}
                    self.assertAllEqual(band_np, band.eval(feed_dict=feed_dict))
