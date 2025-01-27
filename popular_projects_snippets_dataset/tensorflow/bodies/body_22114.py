# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    inputs = [True, True, True, False, True]
    expected_outputs = [1, 2, 2, 1, 1]
    self._test_helper(inputs, expected_outputs)
