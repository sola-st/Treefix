# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id)

for i in range(100):
    source_file = debug_event_pb2.SourceFile(
        host_name="localhost", file_path="/tmp/file_%d.py" % i)
    source_file.lines.append("# File %d" % i)
    writer.WriteSourceFile(source_file)
writer.FlushNonExecutionFiles()

reader = debug_events_reader.DebugDataReader(self.dump_root)
reader.update()
lines = [None] * 100
def read_job_1():
    # Read in the reverse order to enhance randomness of the read access.
    for i in range(49, -1, -1):
        lines[i] = reader.source_lines("localhost", "/tmp/file_%d.py" % i)
def read_job_2():
    for i in range(99, 49, -1):
        lines[i] = reader.source_lines("localhost", "/tmp/file_%d.py" % i)
thread_1 = threading.Thread(target=read_job_1)
thread_2 = threading.Thread(target=read_job_2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
for i in range(100):
    self.assertEqual(lines[i], ["# File %d" % i])
