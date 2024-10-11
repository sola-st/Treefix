# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
if v[0] is None:
    v[0] = variables_lib.Variable(
        random_ops.random_normal([]),
        synchronization=variables_lib.VariableSynchronization.ON_READ)
