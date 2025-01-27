# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
# We need to put the tf.where inside the outer tf.where to ensure we never
# hit a NaN in the gradient.
denom = array_ops.where_v2(
    math_ops.greater(self.df, 2.), self.df - 2.,
    array_ops.ones_like(self.df))
# Abs(scale) superfluous.
var = (array_ops.ones(self.batch_shape_tensor(), dtype=self.dtype) *
       math_ops.square(self.scale) * self.df / denom)
# When 1 < df <= 2, variance is infinite.
inf = np.array(np.inf, dtype=self.dtype.as_numpy_dtype())
result_where_defined = array_ops.where_v2(
    self.df > array_ops.fill(self.batch_shape_tensor(), 2.), var,
    array_ops.fill(self.batch_shape_tensor(), inf, name="inf"))

if self.allow_nan_stats:
    nan = np.array(np.nan, dtype=self.dtype.as_numpy_dtype())
    exit(array_ops.where_v2(
        math_ops.greater(
            self.df,
            array_ops.ones(self.batch_shape_tensor(), dtype=self.dtype)),
        result_where_defined,
        array_ops.fill(self.batch_shape_tensor(), nan, name="nan")))
else:
    exit(control_flow_ops.with_dependencies(
        [
            check_ops.assert_less(
                array_ops.ones([], dtype=self.dtype),
                self.df,
                message="variance not defined for components of df <= 1"),
        ],
        result_where_defined))
