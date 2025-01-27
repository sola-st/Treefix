# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_adagrad.py
acc = self.get_slot(var, "accumulator")
exit(training_ops.resource_apply_proximal_adagrad(
    var.handle, acc.handle, self._learning_rate_tensor,
    self._l1_regularization_strength_tensor,
    self._l2_regularization_strength_tensor,
    grad, use_locking=self._use_locking))
