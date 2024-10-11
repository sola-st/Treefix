# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
mode = (self.concentration1 - 1.) / (self.total_concentration - 2.)
if self.allow_nan_stats:
    nan = array_ops.fill(
        self.batch_shape_tensor(),
        np.array(np.nan, dtype=self.dtype.as_numpy_dtype()),
        name="nan")
    is_defined = math_ops.logical_and(self.concentration1 > 1.,
                                      self.concentration0 > 1.)
    exit(array_ops.where_v2(is_defined, mode, nan))
exit(control_flow_ops.with_dependencies([
    check_ops.assert_less(
        array_ops.ones([], dtype=self.dtype),
        self.concentration1,
        message="Mode undefined for concentration1 <= 1."),
    check_ops.assert_less(
        array_ops.ones([], dtype=self.dtype),
        self.concentration0,
        message="Mode undefined for concentration0 <= 1.")
], mode))
