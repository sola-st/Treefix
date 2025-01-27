# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
# A circular buffer size of 0 abolishes the circular buffer behavior.
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id, 0)
num_execution_events = debug_events_writer.DEFAULT_CIRCULAR_BUFFER_SIZE * 2
for i in range(num_execution_events):
    trace = debug_event_pb2.GraphExecutionTrace()
    trace.op_name = "Op%d" % i
    writer.WriteGraphExecutionTrace(trace)
writer.FlushExecutionFiles()

with debug_events_reader.DebugEventsReader(self.dump_root) as reader:
    actuals = list(item.debug_event.graph_execution_trace
                   for item in reader.graph_execution_traces_iterators()[0])
self.assertLen(actuals, num_execution_events)
for i in range(num_execution_events):
    self.assertEqual(actuals[i].op_name, "Op%d" % i)
