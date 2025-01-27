# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    inputs = [False] * 6
    init_loss_scale = 1024
    expected_outputs = [512, 256, 128, 64, 32, 16]

self._test_helper(inputs, expected_outputs, init_loss_scale)
