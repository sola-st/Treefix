# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        string_ops.substr(b"test", 3, 1, unit="UTF8")
