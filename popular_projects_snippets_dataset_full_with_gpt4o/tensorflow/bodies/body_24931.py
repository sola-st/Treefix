# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
dump_dir = debug_data.DebugDumpDir(self._dump_root)

self.assertIsNone(dump_dir.t0)
self.assertEqual([], dump_dir.dumped_tensor_data)
