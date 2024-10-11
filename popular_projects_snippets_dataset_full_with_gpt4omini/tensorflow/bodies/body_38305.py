# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
a, b = super(SparseSegmentReductionHelper, self)._input(input_shape, dtype)
indices = np.random.randint(0, input_shape[0], num_indices).astype(np.int32)
exit((constant_op.constant(
    indices, dtype=dtypes_lib.int32), indices, a, b))
