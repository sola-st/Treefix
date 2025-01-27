# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
with self.session():
    v = variables.Variable(
        array_ops.zeros(dtype=dtypes.float32, shape=[2**33, 1]))
    n = random_ops.truncated_normal(v.shape)
    self.assertEqual([8589934592, 1], n.shape.as_list())
