# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
circular_buffer_size = -1
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id,
                                               circular_buffer_size)
debugged_graph = debug_event_pb2.DebuggedGraph(graph_id="graph1",
                                               graph_name="graph1")
writer.WriteDebuggedGraph(debugged_graph)

for i in range(100):
    op_name = "Op%d" % i
    graph_op_creation = debug_event_pb2.GraphOpCreation(
        op_type="FooOp", op_name=op_name, graph_id="graph1")
    writer.WriteGraphOpCreation(graph_op_creation)
    trace = debug_event_pb2.GraphExecutionTrace(
        op_name=op_name, tfdbg_context_id="graph1")
    writer.WriteGraphExecutionTrace(trace)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

reader = debug_events_reader.DebugDataReader(self.dump_root)
reader.update()
traces = [None] * 100
def read_job_1():
    digests = reader.graph_execution_traces(digest=True)
    for i in range(49, -1, -1):
        traces[i] = reader.read_graph_execution_trace(digests[i])
def read_job_2():
    digests = reader.graph_execution_traces(digest=True)
    for i in range(99, 49, -1):
        traces[i] = reader.read_graph_execution_trace(digests[i])
thread_1 = threading.Thread(target=read_job_1)
thread_2 = threading.Thread(target=read_job_2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
for i in range(100):
    self.assertEqual(traces[i].op_name, "Op%d" % i)
