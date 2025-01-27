# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
writer = debug_events_writer.DebugEventsWriter(
    self.dump_root, self.tfdbg_run_id, circular_buffer_size=-1)
for i in range(5):
    execution = debug_event_pb2.Execution(op_type="OpType%d" % i)
    writer.WriteExecution(execution)
writer.FlushExecutionFiles()
writer.Close()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    executions = reader.executions(begin=begin, end=end)
self.assertLen(executions, expected_end - expected_begin)
self.assertEqual(executions[0].op_type, "OpType%d" % expected_begin)
self.assertEqual(executions[-1].op_type, "OpType%d" % (expected_end - 1))
