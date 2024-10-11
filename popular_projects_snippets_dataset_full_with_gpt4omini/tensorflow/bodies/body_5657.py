# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
# In multi client setup, worker_devices is just the devices on that
# worker.
worker_device_id = ctx.replica_id_in_sync_group % len(worker_devices)
with ops.device(worker_devices[worker_device_id]):
    exit(op_type(1.0))
