# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
assertion = check_ops.assert_shapes([])
with ops.control_dependencies([assertion]):
    out = array_ops.identity(0)
self.evaluate(out)
