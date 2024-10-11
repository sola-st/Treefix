# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
mean = self.loc * array_ops.ones(self.batch_shape_tensor(),
                                 dtype=self.dtype)
if self.allow_nan_stats:
    nan = np.array(np.nan, dtype=self.dtype.as_numpy_dtype())
    exit(array_ops.where_v2(
        math_ops.greater(
            self.df,
            array_ops.ones(self.batch_shape_tensor(), dtype=self.dtype)),
        mean, array_ops.fill(self.batch_shape_tensor(), nan, name="nan")))
else:
    exit(control_flow_ops.with_dependencies(
        [
            check_ops.assert_less(
                array_ops.ones([], dtype=self.dtype),
                self.df,
                message="mean not defined for components of df <= 1"),
        ],
        mean))
