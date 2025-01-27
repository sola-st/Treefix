# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id)
num_execution_events = debug_events_writer.DEFAULT_CIRCULAR_BUFFER_SIZE * 2
for i in range(num_execution_events):
    execution = debug_event_pb2.Execution()
    execution.op_type = "OpType%d" % i
    writer.WriteExecution(execution)

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    # Before FlushExecutionFiles() is called. No data should have been written
    # to the file.
    reader.update()
    self.assertFalse(reader.executions())

    writer.FlushExecutionFiles()
    reader.update()
    executions = reader.executions()
    for i, execution in enumerate(executions):
        self.assertEqual(
            execution.op_type,
            "OpType%d" % (i + debug_events_writer.DEFAULT_CIRCULAR_BUFFER_SIZE))
