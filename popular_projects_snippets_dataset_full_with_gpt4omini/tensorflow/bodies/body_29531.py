# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/identity_n_op_py_test.py
source = [b"A", b"b", b"C", b"d", b"E", b"f"]
[value] = self.evaluate(array_ops.identity_n([source]))
self.assertAllEqual(source, value)
