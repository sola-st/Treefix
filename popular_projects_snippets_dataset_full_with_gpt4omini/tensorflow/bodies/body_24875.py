# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
while True:
    if writer_state["done"]:
        break
    op_name = "Op%d" % writer_state["counter"]
    graph_op_creation = debug_event_pb2.GraphOpCreation(
        op_type="FooOp", op_name=op_name, graph_id="graph1")
    writer.WriteGraphOpCreation(graph_op_creation)
    trace = debug_event_pb2.GraphExecutionTrace(
        op_name=op_name, tfdbg_context_id="graph1")
    writer.WriteGraphExecutionTrace(trace)
    writer_state["counter"] += 1
    writer.FlushNonExecutionFiles()
    writer.FlushExecutionFiles()
    reader.update()
