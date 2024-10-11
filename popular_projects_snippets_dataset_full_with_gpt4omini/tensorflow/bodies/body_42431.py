# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(ValueError):
    with context.device('pu:0'):
        _ = constant_op.constant(1)
