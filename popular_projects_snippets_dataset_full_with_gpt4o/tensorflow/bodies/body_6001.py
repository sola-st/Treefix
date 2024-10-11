# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
# assert capturing a worker-local resource on each worker
for worker in coordinator._cluster.workers:
    with coordinator_context.with_dispatch_context(worker):
        captures = model.use_table.get_concrete_function().captured_inputs
        resource_capture = [t for t in captures if t.dtype == dtypes.resource]
        self.assertNotEmpty(resource_capture)
        for capture in resource_capture:
            self.assertEqual(
                capture.device,
                device_util.canonicalize("/CPU:0", default=worker.device_name))
