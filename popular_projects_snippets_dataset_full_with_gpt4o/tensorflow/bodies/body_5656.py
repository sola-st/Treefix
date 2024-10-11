# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")
def value_fn(ctx):
    del ctx
    exit(constant_op.constant(1.0))
distributed_values = (
    distribution.experimental_distribute_values_from_function(value_fn))
default_device = array_ops.identity(constant_op.constant(1.0)).device
for i in range(len(distribution.extended.worker_devices)):
    self.assertAllEqual(distributed_values._values[i].device, default_device)
