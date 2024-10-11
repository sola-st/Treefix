# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
with distribution.scope():
    v = variables_lib.Variable(
        1., synchronization=synchronization, aggregation=aggregation)
self.assertIsInstance(v, variables_lib.Variable)
