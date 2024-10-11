# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
var = variables.Variable(
    initial_value=0.0, dtype=var_dtype, name=var_name)
self.assertIn('worker', var.device)
exit(var)
