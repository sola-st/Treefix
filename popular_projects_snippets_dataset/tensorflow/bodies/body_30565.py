# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with self.session():
    self.assertAllEqual(np.arange(5), math_ops.range(5))
