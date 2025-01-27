# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
stack_frame = debug_event_pb2.StackFrameWithId()
with stack_frame_state["lock"]:
    stack_frame.id = "stack_frame_%d" % stack_frame_state["counter"]
    stack_frame_state["counter"] += 1
writer.WriteStackFrameWithId(stack_frame)
# More-frequent-than-necessary concurrent flushing is not recommended,
# but tolerated.
writer.FlushNonExecutionFiles()
