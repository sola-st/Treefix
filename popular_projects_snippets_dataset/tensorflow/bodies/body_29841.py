# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with ops.Graph().as_default():
    large_array = np.zeros((512, 1024, 1024), dtype=np.float32)
    with self.assertRaisesRegex(
        ValueError,
        "Cannot create a tensor proto whose content is larger than 2GB."):
        c = constant_op.constant(large_array)
