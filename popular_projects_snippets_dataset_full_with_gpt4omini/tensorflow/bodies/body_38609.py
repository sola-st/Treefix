# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
# A singleton dimension is a dimension i with shape[i] == 1. Such dimensions
# can be collapsed and expanded using reshape without changing the
# underlying data storage. If all non-singleton dimensions remain in
# ascending order, the shuffled singletons will be transposed by a reshape,
# saving a memory allocation & copy. Since this gets a special code-path in
# transpose_op.cc, we test that the codepath is exercised and the results
# are as expected; we do not test that we save the memory allocation and
# copy here.
for shape in [[2, 1, 2], [2, 1, 2, 1, 1, 2], [1, 2, 2, 1, 1, 1],
              [1, 1, 1, 2, 2, 2], [2, 2, 1, 1, 1]]:
    with self.subTest(shape=shape):
        self._compare_cpu_gpu(
            np.arange(np.prod(shape)).reshape(shape).astype(np.float32))
