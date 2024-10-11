# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
writer = dumping_callback.enable_dump_debug_info(self.dump_root)
# Run a simple eager execution event, so that the source-file contents are
# dumped.
self.assertAllClose(math_ops.truediv(7.0, 1.0 / 6.0), 42.0)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()
with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    with open(_current_file_full_path, "rt") as f:
        file_lines = f.read().split("\n")
    self.assertEqual(
        reader.source_lines(_host_name, _current_file_full_path), file_lines)
