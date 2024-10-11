# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
del first_arg  # Just here to make sure we're not relying on arg position.

if variable is not None:
    self.assertIsInstance(variable, tpu_values.TPUDistributedVariable)
