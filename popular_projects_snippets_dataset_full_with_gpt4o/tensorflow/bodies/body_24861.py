# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
# A circular buffer size of 0 abolishes the circular buffer behavior.
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id, 0)
num_execution_events = debug_events_writer.DEFAULT_CIRCULAR_BUFFER_SIZE * 2
for i in range(num_execution_events):
    execution = debug_event_pb2.Execution()
    execution.op_type = "OpType%d" % i
    writer.WriteExecution(execution)
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    executions = reader.executions()
    self.assertLen(executions, num_execution_events)
    for i, execution in enumerate(executions):
        self.assertEqual(execution.op_type, "OpType%d" % i)
