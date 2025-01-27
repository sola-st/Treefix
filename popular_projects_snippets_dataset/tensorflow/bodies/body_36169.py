# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
initializer = np.array(1.0)
# Multiply a * 1 each time
with self.assertRaisesRegex(
    ValueError, "two structures don't have the same nested structure"):
    functional_ops.scan(lambda a, x: (a, -a), elems, initializer)
