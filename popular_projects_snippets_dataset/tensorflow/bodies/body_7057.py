# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
if context.executing_eagerly():
    exit(self.get_var_on_current_device().value())
else:
    exit(super(PackedDistributedVariable, self)._read_variable_op())
