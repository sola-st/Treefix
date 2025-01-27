# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with self.cached_session():
    with self.assertRaisesRegex(ValueError, "`maxlen` must be scalar"):
        array_ops.sequence_mask([10, 20], [10, 20])
