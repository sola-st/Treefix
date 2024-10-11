# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
variables = []
for device in self.devices:
    with ops.device(device):
        variables.append(
            variables_lib.Variable(initial_value, **kwargs))
exit(values_v2.DistributedVariable(variables))
