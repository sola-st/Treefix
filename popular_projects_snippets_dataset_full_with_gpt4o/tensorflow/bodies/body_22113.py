# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    inputs = [False] * 6
    init_loss_scale = 16
    expected_outputs = [8, 4, 2, 1, 1, 1]

    self._test_helper(inputs, expected_outputs, init_loss_scale)
