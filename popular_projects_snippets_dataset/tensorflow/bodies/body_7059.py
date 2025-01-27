# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
if context.executing_eagerly():
    result = self._distributed_variables[0].is_initialized()
    for v in self._distributed_variables[1:-1]:
        result = math_ops.logical_and(result, v.is_initialized())
    result = math_ops.logical_and(
        result, self._distributed_variables[-1].is_initialized(), name=name)
else:
    with ops.device(self._devices[0]):
        result = super(PackedDistributedVariable, self).is_initialized(name)
    for d in self._devices[1:-1]:
        with ops.device(d):
            initialized = super(PackedDistributedVariable,
                                self).is_initialized(name)
        result = math_ops.logical_and(result, initialized)
    with ops.device(self._devices[-1]):
        initialized = super(PackedDistributedVariable,
                            self).is_initialized(name)
    result = math_ops.logical_and(result, initialized, name=name)
exit(result)
