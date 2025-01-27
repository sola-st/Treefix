# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id)
num_op_creations = 10
for i in range(num_op_creations):
    graph_op_creation = debug_event_pb2.GraphOpCreation()
    graph_op_creation.op_type = "Conv2D"
    graph_op_creation.op_name = "Conv2D_%d" % i
    writer.WriteGraphOpCreation(graph_op_creation)
debugged_graph = debug_event_pb2.DebuggedGraph()
debugged_graph.graph_id = "deadbeaf"
debugged_graph.graph_name = "MyGraph1"
writer.WriteDebuggedGraph(debugged_graph)
writer.FlushNonExecutionFiles()

reader = debug_events_reader.DebugEventsReader(self.dump_root)
actuals = list(item.debug_event for item in reader.graphs_iterator())
self.assertLen(actuals, num_op_creations + 1)
for i in range(num_op_creations):
    self.assertEqual(actuals[i].graph_op_creation.op_type, "Conv2D")
    self.assertEqual(actuals[i].graph_op_creation.op_name, "Conv2D_%d" % i)
self.assertEqual(actuals[num_op_creations].debugged_graph.graph_id,
                 "deadbeaf")
