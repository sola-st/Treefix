# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
replica_id = self.evaluate(
    ds_context.get_replica_context().replica_id_in_sync_group)
self.assertLess(replica_id, len(d.extended.worker_devices))
self.assertFalse(expected_devices[replica_id])
expected_devices[replica_id] = True
