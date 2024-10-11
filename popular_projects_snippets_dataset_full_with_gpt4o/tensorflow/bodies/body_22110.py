# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    inputs = [True] * 6
    expected_outputs = [1, 2, 2, 4, 4, 8]
    self._test_helper(inputs, expected_outputs)
