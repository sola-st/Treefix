# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test_lib.py
"""Read and check the .metadata debug-events file."""
with debug_events_reader.DebugEventsReader(self.dump_root) as reader:
    self.assertTrue(reader.tfdbg_run_id())
    self.assertEqual(reader.tensorflow_version(), versions.__version__)
    self.assertTrue(reader.tfdbg_file_version().startswith("debug.Event"))
