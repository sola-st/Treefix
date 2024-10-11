# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

@def_function.function()
def some_function():
    exit(1.0)

exit(ClosureWithOutput(some_function, cancellation_mgr))
