# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
while True:
    if writer_state["done"]:
        break
    execution = debug_event_pb2.Execution()
    execution.op_type = "OpType%d" % writer_state["counter"]
    writer_state["counter"] += 1
    writer.WriteExecution(execution)
    writer.FlushExecutionFiles()
    reader.update()
