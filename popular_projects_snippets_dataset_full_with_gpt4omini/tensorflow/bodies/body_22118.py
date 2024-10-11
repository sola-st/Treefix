# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    init_loss_scale = 4
    multiplier = 3
    inputs = [True, True, False, True, True]
    expected_outputs = [4, 12, 4, 4, 12]
    self._test_helper(
        inputs, expected_outputs, init_loss_scale, multiplier=multiplier)
