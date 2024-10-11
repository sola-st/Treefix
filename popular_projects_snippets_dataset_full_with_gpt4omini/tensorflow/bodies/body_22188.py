# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
"""Check if `_loss_scale` dynamically manages the loss scale."""
exit(isinstance(self._loss_scale, loss_scale_module.DynamicLossScale))
