# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id)
num_execution_events = debug_events_writer.DEFAULT_CIRCULAR_BUFFER_SIZE * 2
for i in range(num_execution_events):
    trace = debug_event_pb2.GraphExecutionTrace()
    trace.op_name = "Op%d" % i
    writer.WriteGraphExecutionTrace(trace)

with debug_events_reader.DebugEventsReader(self.dump_root) as reader:
    actuals = list(reader.graph_execution_traces_iterators()[0])
    # Before FlushExecutionFiles() is called. No data should have been written
    # to the file.
    self.assertEmpty(actuals)

    writer.FlushExecutionFiles()
    actuals = list(item.debug_event.graph_execution_trace
                   for item in reader.graph_execution_traces_iterators()[0])
    self.assertLen(actuals, debug_events_writer.DEFAULT_CIRCULAR_BUFFER_SIZE)
    for i in range(debug_events_writer.DEFAULT_CIRCULAR_BUFFER_SIZE):
        self.assertEqual(
            actuals[i].op_name,
            "Op%d" % (i + debug_events_writer.DEFAULT_CIRCULAR_BUFFER_SIZE))
