# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    init_loss_scale = 1
    increment_period = 1

    inputs = [True, False] * 4 + [True]
    expected_outputs = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    self._test_helper(inputs, expected_outputs, init_loss_scale,
                      increment_period)
