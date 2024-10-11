# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
with d.scope():
    expected_devices = [False] * len(d.extended.worker_devices)

    def mark_devices_fn():
        replica_id = self.evaluate(
            ds_context.get_replica_context().replica_id_in_sync_group)
        self.assertLess(replica_id, len(d.extended.worker_devices))
        self.assertFalse(expected_devices[replica_id])
        expected_devices[replica_id] = True

    d.extended.call_for_each_replica(mark_devices_fn)
    self.assertAllEqual(expected_devices,
                        [True] * len(d.extended.worker_devices))
