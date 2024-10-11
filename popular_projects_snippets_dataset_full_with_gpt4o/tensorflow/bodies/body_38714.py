# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/histogram_ops_test.py
value_range = [0.0, 5.0]
values = [[-1.0, 0.0, 1.5], [2.0, 5.0, 15]]
expected_bin_counts = [2, 1, 1, 0, 2]
placeholder = array_ops.placeholder(dtypes.int32)
with self.session():
    hist = histogram_ops.histogram_fixed_width(values, value_range, nbins=5)
    self.assertAllEqual(hist.shape.as_list(), (5,))
    self.assertEqual(dtypes.int32, hist.dtype)
    self.assertAllClose(expected_bin_counts, self.evaluate(hist))

    hist = histogram_ops.histogram_fixed_width(
        values, value_range, nbins=placeholder)
    self.assertEqual(hist.shape.ndims, 1)
    self.assertIs(hist.shape.dims[0].value, None)
    self.assertEqual(dtypes.int32, hist.dtype)
    self.assertAllClose(expected_bin_counts, hist.eval({placeholder: 5}))
