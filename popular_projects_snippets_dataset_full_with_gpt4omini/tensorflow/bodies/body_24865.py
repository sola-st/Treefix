# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
with graph_execution_trace_state["lock"]:
    op_name = "Op%d" % graph_execution_trace_state["counter"]
    graph_op_creation = debug_event_pb2.GraphOpCreation(
        op_type="FooOp", op_name=op_name, graph_id="graph1")
    trace = debug_event_pb2.GraphExecutionTrace(
        op_name=op_name, tfdbg_context_id="graph1")
    graph_execution_trace_state["counter"] += 1
writer.WriteGraphOpCreation(graph_op_creation)
writer.WriteGraphExecutionTrace(trace)
