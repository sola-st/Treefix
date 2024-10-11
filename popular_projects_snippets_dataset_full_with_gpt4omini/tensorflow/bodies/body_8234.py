# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/gce_failure_handler_test.py
self.v = variables_lib.Variable(
    0.,
    synchronization=variables_lib.VariableSynchronization.ON_WRITE,
    aggregation=variables_lib.VariableAggregation.SUM)
