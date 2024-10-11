# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
execution = debug_event_pb2.Execution()
with execution_state["lock"]:
    execution.op_type = "OpType%d" % execution_state["counter"]
    execution_state["counter"] += 1
writer.WriteExecution(execution)
