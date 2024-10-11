# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
variables = []
for device in strategy.extended.parameter_devices:
    with ops.device(device):
        variables.append(variables_lib.Variable(initial_value, **kwargs))
exit(values_v2.DistributedVariable(
    variables, enable_packed_handle=enable_packed_handle))
