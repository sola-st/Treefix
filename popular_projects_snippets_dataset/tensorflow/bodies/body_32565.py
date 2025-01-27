# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.constant([1, 1], name="x")
assertion = check_ops.assert_shapes([(x, None)])
with ops.control_dependencies([assertion]):
    out = array_ops.identity(x)
self.evaluate(out)
