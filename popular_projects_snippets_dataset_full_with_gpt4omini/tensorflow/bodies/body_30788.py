# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/inplace_ops_test.py
with test_util.use_gpu():
    x = array_ops.ones([2, 3])
    y = inplace_ops.alias_inplace_add(x, [0], [[1, 2, 3]])
    with ops.control_dependencies([y]):
        z = array_ops.identity(x)
        _, vy, vz = self.evaluate([x, y, z])
    self.assertAllClose(vy, vz)
