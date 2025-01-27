# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
if context.executing_eagerly():
    exit(self.get_var_on_current_device()._dense_var_to_tensor(  # pylint: disable=protected-access
        dtype=dtype,
        name=name,
        as_ref=as_ref))
else:
    exit(super(PackedDistributedVariable, self)._dense_var_to_tensor(  # pylint: disable=protected-access
        dtype=dtype,
        name=name,
        as_ref=as_ref))
