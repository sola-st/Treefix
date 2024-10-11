# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
# To simulate a multi-host data dump, we first generate file sets in two
# different directories, with different tfdbg_run_ids, and then combine
# them.
for i in range(2):
    writer = debug_events_writer.DebugEventsWriter(
        os.path.join(self.dump_root, str(i)),
        "run_id_%d" % i,
        circular_buffer_size=-1)
    writer.FlushNonExecutionFiles()
    writer.FlushExecutionFiles()

# Move all files from the subdirectory /1 to subdirectory /0.
dump_root_0 = os.path.join(self.dump_root, "0")
src_paths = glob.glob(os.path.join(self.dump_root, "1", "*"))
for src_path in src_paths:
    dst_path = os.path.join(
        dump_root_0,
        # Rename the file set to avoid file name collision.
        re.sub(r"(tfdbg_events\.\d+)", r"\g<1>1", os.path.basename(src_path)))
    os.rename(src_path, dst_path)

with self.assertRaisesRegex(ValueError,
                            r"Found multiple \(2\) tfdbg2 runs"):
    debug_events_reader.DebugDataReader(dump_root_0)
