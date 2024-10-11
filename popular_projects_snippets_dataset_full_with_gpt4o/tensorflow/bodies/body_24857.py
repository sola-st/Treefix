# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
graph_op_creation = debug_event_pb2.GraphOpCreation()
with graph_op_state["lock"]:
    graph_op_creation.op_name = "Op%d" % graph_op_state["counter"]
    graph_op_state["counter"] += 1
writer.WriteGraphOpCreation(graph_op_creation)
# More-frequent-than-necessary concurrent flushing is not recommended,
# but tolerated.
writer.FlushNonExecutionFiles()
