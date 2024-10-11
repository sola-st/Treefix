# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
self.w = variables.Variable(
    initial_value=random_ops.random_uniform((10, 10)), dtype=dtypes.float32)
self.iterations = variables.Variable(initial_value=0, dtype=dtypes.int32)
# Allow external control to make the model run its train_fn in an infinite
# loop. This allows us to reliably test worker preemption in the middle of
# function execution.
self.do_infinite_step = variables.Variable(False)

self.rebuild_iterators()
