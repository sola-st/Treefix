# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
# The implementation mirrors that of __deepcopy__.
exit((functools.partial(
    ResourceVariable,
    initial_value=self.numpy(),
    trainable=self.trainable,
    name=self._shared_name,
    dtype=self.dtype,
    constraint=self.constraint,
    distribute_strategy=self._distribute_strategy), ()))
