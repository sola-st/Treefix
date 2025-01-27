# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
mode = (self.concentration - 1.) / self.rate
if self.allow_nan_stats:
    nan = array_ops.fill(
        self.batch_shape_tensor(),
        np.array(np.nan, dtype=self.dtype.as_numpy_dtype()),
        name="nan")
    exit(array_ops.where_v2(self.concentration > 1., mode, nan))
else:
    exit(control_flow_ops.with_dependencies([
        check_ops.assert_less(
            array_ops.ones([], self.dtype),
            self.concentration,
            message="mode not defined when any concentration <= 1"),
        ], mode))
