# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
circular_buffer_size = 5
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id,
                                               circular_buffer_size)
debugged_graph = debug_event_pb2.DebuggedGraph(graph_id="graph1",
                                               graph_name="graph1")
writer.WriteDebuggedGraph(debugged_graph)

execution_state = {"counter": 0, "lock": threading.Lock()}

def write_execution():
    execution = debug_event_pb2.Execution()
    with execution_state["lock"]:
        execution.op_type = "OpType%d" % execution_state["counter"]
        execution_state["counter"] += 1
    writer.WriteExecution(execution)

graph_execution_trace_state = {"counter": 0, "lock": threading.Lock()}

def write_graph_execution_trace():
    with graph_execution_trace_state["lock"]:
        op_name = "Op%d" % graph_execution_trace_state["counter"]
        graph_op_creation = debug_event_pb2.GraphOpCreation(
            op_type="FooOp", op_name=op_name, graph_id="graph1")
        trace = debug_event_pb2.GraphExecutionTrace(
            op_name=op_name, tfdbg_context_id="graph1")
        graph_execution_trace_state["counter"] += 1
    writer.WriteGraphOpCreation(graph_op_creation)
    writer.WriteGraphExecutionTrace(trace)

threads = []
for i in range(circular_buffer_size * 4):
    if i % 2 == 0:
        target = write_execution
    else:
        target = write_graph_execution_trace
    thread = threading.Thread(target=target)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    # Verify the content of the .execution file.
    executions = reader.executions()
    executed_op_types = [execution.op_type for execution in executions]
    self.assertLen(executed_op_types, circular_buffer_size)
    self.assertLen(executed_op_types, len(set(executed_op_types)))

    # Verify the content of the .graph_execution_traces file.
    op_names = [trace.op_name for trace in reader.graph_execution_traces()]
    self.assertLen(op_names, circular_buffer_size)
    self.assertLen(op_names, len(set(op_names)))
