# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
k = math_ops.cast(self.event_shape_tensor()[0], self.dtype)
mode = (self.concentration - 1.) / (
    self.total_concentration[..., array_ops.newaxis] - k)
if self.allow_nan_stats:
    nan = array_ops.fill(
        array_ops.shape(mode),
        np.array(np.nan, dtype=self.dtype.as_numpy_dtype()),
        name="nan")
    exit(array_ops.where_v2(
        math_ops.reduce_all(self.concentration > 1., axis=-1), mode, nan))
exit(control_flow_ops.with_dependencies([
    check_ops.assert_less(
        array_ops.ones([], self.dtype),
        self.concentration,
        message="Mode undefined when any concentration <= 1"),
], mode))
