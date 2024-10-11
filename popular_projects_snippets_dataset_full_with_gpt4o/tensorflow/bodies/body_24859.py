# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
t0 = time.time()
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id)
writer.Close()
with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    self.assertIsInstance(reader.starting_wall_time(), float)
    self.assertGreaterEqual(reader.starting_wall_time(), t0)
    self.assertEqual(reader.tensorflow_version(), versions.__version__)
    self.assertTrue(reader.tfdbg_run_id())
