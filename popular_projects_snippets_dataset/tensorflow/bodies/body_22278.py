# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_da.py
self._learning_rate_tensor = ops.convert_to_tensor(
    self._learning_rate, name="learning_rate")
# Performance optimization so that worker creates a copy of the global step
# to avoid overloading the parameter server holding the global step.
with ops.colocate_with(self._learning_rate_tensor):
    self._global_step_on_worker = array_ops.identity(self._global_step) + 1
