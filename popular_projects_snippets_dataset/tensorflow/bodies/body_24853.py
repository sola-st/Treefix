# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id)
num_protos = 10
for i in range(num_protos):
    source_file = debug_event_pb2.SourceFile()
    source_file.file_path = "/home/tf2user/main.py"
    source_file.host_name = "machine.cluster"
    source_file.lines.append("print(%d)" % i)
    writer.WriteSourceFile(source_file)

    stack_frame = debug_event_pb2.StackFrameWithId()
    stack_frame.id = "stack_%d" % i
    stack_frame.file_line_col.file_index = i * 10
    writer.WriteStackFrameWithId(stack_frame)

writer.FlushNonExecutionFiles()

with debug_events_reader.DebugEventsReader(self.dump_root) as reader:
    actuals = list(item.debug_event.source_file
                   for item in reader.source_files_iterator())
    self.assertLen(actuals, num_protos)
    for i in range(num_protos):
        self.assertEqual(actuals[i].file_path, "/home/tf2user/main.py")
        self.assertEqual(actuals[i].host_name, "machine.cluster")
        self.assertEqual(actuals[i].lines, ["print(%d)" % i])

    actuals = list(item.debug_event.stack_frame_with_id
                   for item in reader.stack_frames_iterator())
    self.assertLen(actuals, num_protos)
    for i in range(num_protos):
        self.assertEqual(actuals[i].id, "stack_%d" % i)
        self.assertEqual(actuals[i].file_line_col.file_index, i * 10)
