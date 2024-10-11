# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
with strategy_fn().scope():
    init_loss_scale = np.finfo(np.float32).max / 4
    max_float = np.finfo(np.float32).max

    inputs = [True] * 6
    # Output is capped the 2nd time it doubles.
    expected_outputs = [
        init_loss_scale, init_loss_scale * 2, init_loss_scale * 2, max_float,
        max_float, max_float
    ]

    self._test_helper(inputs, expected_outputs, init_loss_scale)
