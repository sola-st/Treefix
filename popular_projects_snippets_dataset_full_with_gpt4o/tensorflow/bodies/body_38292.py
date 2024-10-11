# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Each item is np_op1, np_op2, tf_op, initial_value functor
self.ops_list = [(np.add, None,
                  math_ops.unsorted_segment_sum, lambda t: 0),
                 (self._mean_cum_op, self._mean_reduce_op,
                  math_ops.unsorted_segment_mean, lambda t: 0),
                 (self._mean_cum_op, self._sqrt_n_reduce_op,
                  math_ops.unsorted_segment_sqrt_n, lambda t: 0),
                 (np.ndarray.__mul__, None,
                  math_ops.unsorted_segment_prod, lambda t: 1),
                 (np.minimum, None,
                  math_ops.unsorted_segment_min, lambda t: t.max),
                 (np.maximum, None,
                  math_ops.unsorted_segment_max, lambda t: t.min)]

# A subset of ops has been enabled for complex numbers
self.complex_ops_list = [(np.add, None,
                          math_ops.unsorted_segment_sum, lambda t: 0),
                         (np.ndarray.__mul__, None,
                          math_ops.unsorted_segment_prod, lambda t: 1)]
self.differentiable_dtypes = [dtypes_lib.float16, dtypes_lib.float32,
                              dtypes_lib.float64]
self.all_dtypes = (self.differentiable_dtypes +
                   [dtypes_lib.bfloat16,
                    dtypes_lib.int64, dtypes_lib.int32,
                    dtypes_lib.complex64, dtypes_lib.complex128])
super(UnsortedSegmentTest, self).__init__(methodName=methodName)
