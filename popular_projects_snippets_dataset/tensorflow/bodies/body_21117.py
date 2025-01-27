# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad.py
acc = self.get_slot(var, "accumulator")
exit(training_ops.sparse_apply_adagrad(
    var,
    acc,
    math_ops.cast(self._learning_rate_tensor, var.dtype.base_dtype),
    grad.values,
    grad.indices,
    use_locking=self._use_locking))
