# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    init_loss_scale = 4
    inputs = [
        False, True, True, True, False, True, False, True, True, True, False
    ]
    expected_outputs = [2, 2, 4, 4, 2, 2, 1, 1, 2, 2, 1]
    self._test_helper(inputs, expected_outputs, init_loss_scale)
