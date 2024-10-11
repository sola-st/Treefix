# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
value_specs = [tensor_spec_per_input for _ in range(num_replicas)]
exit(values.PerReplicaSpec(*value_specs))
