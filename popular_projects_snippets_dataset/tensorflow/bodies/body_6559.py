# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
with distribution.scope():
    mirrored = variable_scope.variable(1.0)
    sync_on_read = variable_scope.variable(
        1.0, synchronization=variable_scope.VariableSynchronization.ON_READ)
    self.assertIs(distribution, mirrored.distribute_strategy)
    self.assertIs(distribution, sync_on_read.distribute_strategy)
