# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
super(DebugIdentityV2OpTest, self).setUp()
# Testing using a small circular-buffer size.
self.circular_buffer_size = 4
self.tfdbg_run_id = "test_tfdbg_run"
self.writer = debug_events_writer.DebugEventsWriter(
    self.dump_root, self.tfdbg_run_id, self.circular_buffer_size)
