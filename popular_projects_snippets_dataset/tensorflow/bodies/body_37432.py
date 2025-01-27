# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
meta = config_pb2.RunMetadata()
try:
    summary_ops.set_step(42)
    event = self.run_metadata_graphs(name='my_name', data=meta)
    self.assertEqual(42, event.step)
finally:
    # Reset to default state for other tests.
    summary_ops.set_step(None)
