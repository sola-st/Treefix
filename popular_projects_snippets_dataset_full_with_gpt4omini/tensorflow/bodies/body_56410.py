# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
# This does not test any ops are deterministic, because that is tested by
# many kernel tests.
try:
    config.disable_op_determinism()
    self.assertFalse(config.is_op_determinism_enabled())
    config.enable_op_determinism()
    self.assertTrue(config.is_op_determinism_enabled())
finally:
    config.disable_op_determinism()
