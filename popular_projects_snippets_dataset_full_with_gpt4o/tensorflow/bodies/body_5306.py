# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
self._distributed_variable = distributed_variable
if not self._distributed_variable._policy:
    raise ValueError(
        "The VariablePolicy of the argument `distributed_variable` must be "
        "set to create a _DistributedVariableSaveable. Please set it via "
        "the `var_policy` argument in the constructor of DistributedVariable."
    )
tensor, spec = distributed_variable._policy.get_saveable(
    distributed_variable, primary_variable, name)
super(_DistributedVariableSaveable, self).__init__(tensor, spec, name)
