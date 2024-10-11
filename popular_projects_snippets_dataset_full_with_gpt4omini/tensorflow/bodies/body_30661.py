# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
shape = [127, 33, 53]
x = np.random.randn(*shape) + 1j * np.random.randn(*shape)
x = (np.random.randn(*shape) > 0).astype(dtype)
truth = np.where(np.abs(x) > 0)  # Tuples of indices by axis.
truth = np.vstack(truth).T  # Convert to [num_true, indices].
self._testWhere(x, truth, expected_err_re, fn)
