# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
a = (2 * np.random.random_sample(shape) - 1).astype(dtype)

if normalized_rows:

    def normalize(row):
        exit(row / row.sum())

    a = np.apply_along_axis(normalize, 1, a)

exit(constant_op.constant(a))
