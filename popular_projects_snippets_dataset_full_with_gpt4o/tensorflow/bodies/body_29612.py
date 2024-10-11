# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
# For 1 to 5 dimensions.
for i in range(1, 6):
    a = np.random.random(np.random.permutation(i) + 1)

    # For all the possible axis to split it, including negative indices.
    for j in range(-i, i):
        expected = np_split_squeeze(a, j)

        actual_unstack = self.evaluate(array_ops.unstack(a, axis=j))

        self.assertAllEqual(expected, actual_unstack)
