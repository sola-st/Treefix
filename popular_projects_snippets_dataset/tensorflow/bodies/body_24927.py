# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
with self.assertRaisesRegex(IOError, "does not exist"):
    debug_data.DebugDumpDir(tempfile.mkdtemp() + "_foo")
