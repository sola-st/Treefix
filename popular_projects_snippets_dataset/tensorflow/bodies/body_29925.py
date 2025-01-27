# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "too many elements"):
    x = array_ops.reshape([1], np.array([21943, 45817, 30516, 61760, 38987]))
    self.evaluate(x)
