# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with self.assertRaisesRegex(Exception,
                            "must be a tensor with a single value"):
    array_ops.expand_dims(1, axis=[0, 1])
