# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Initializes a `NanTensorHook`.

    Args:
      loss_tensor: `Tensor`, the loss tensor.
      fail_on_nan_loss: `bool`, whether to raise exception when loss is NaN.
    """
self._loss_tensor = loss_tensor
self._fail_on_nan_loss = fail_on_nan_loss
