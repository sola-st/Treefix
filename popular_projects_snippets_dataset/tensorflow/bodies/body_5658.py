# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")
worker_devices = distribution.extended.worker_devices
def value_fn(ctx):
    # In multi client setup, worker_devices is just the devices on that
    # worker.
    worker_device_id = ctx.replica_id_in_sync_group % len(worker_devices)
    with ops.device(worker_devices[worker_device_id]):
        exit(op_type(1.0))

distributed_values = (
    distribution.experimental_distribute_values_from_function(value_fn))
for i in range(len(distribution.extended.worker_devices)):
    self.assertAllEqual(distributed_values._values[i].device,
                        worker_devices[i])
