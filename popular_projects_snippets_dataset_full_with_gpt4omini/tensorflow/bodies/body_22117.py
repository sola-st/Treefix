# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    init_loss_scale = 32
    increment_period = 2

    inputs = [True, False] * 3 + [True]
    expected_outputs = [32, 16, 16, 8, 8, 4, 4]
    self._test_helper(inputs, expected_outputs, init_loss_scale,
                      increment_period)
