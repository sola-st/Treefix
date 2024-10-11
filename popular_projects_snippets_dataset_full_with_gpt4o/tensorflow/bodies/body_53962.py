# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
with self.assertRaisesRegex(ValueError, r"is expected to be callable"):
    op_callbacks.add_op_callback(1337)
