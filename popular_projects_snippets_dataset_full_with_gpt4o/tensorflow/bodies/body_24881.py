# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
writer = debug_events_writer.DebugEventsWriter(
    self.dump_root, self.tfdbg_run_id, circular_buffer_size=-1)
debugged_graph = debug_event_pb2.DebuggedGraph(
    graph_id="graph1", graph_name="graph1")
writer.WriteDebuggedGraph(debugged_graph)
for i in range(5):
    op_name = "Op_%d" % i
    graph_op_creation = debug_event_pb2.GraphOpCreation(
        op_name=op_name, graph_id="graph1")
    writer.WriteGraphOpCreation(graph_op_creation)
    trace = debug_event_pb2.GraphExecutionTrace(
        op_name=op_name, tfdbg_context_id="graph1")
    writer.WriteGraphExecutionTrace(trace)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()
writer.Close()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    traces = reader.graph_execution_traces(begin=begin, end=end)
self.assertLen(traces, expected_end - expected_begin)
self.assertEqual(traces[0].op_name, "Op_%d" % expected_begin)
self.assertEqual(traces[-1].op_name, "Op_%d" % (expected_end - 1))
