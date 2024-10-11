# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
if context.executing_eagerly():
    exit(update_fn(self.get_var_on_current_device(), value, **kwargs))
else:
    exit(update_fn(super(PackedDistributedVariable, self), value, **kwargs))
