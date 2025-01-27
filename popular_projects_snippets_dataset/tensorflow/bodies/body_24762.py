# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer.py
"""Write a StackFrameWithId proto with the writer.

    Args:
      stack_frame_with_id: A StackFrameWithId proto, describing the content a
        stack frame involved in the execution of the debugged TensorFlow
        program.
    """
debug_event = debug_event_pb2.DebugEvent(
    stack_frame_with_id=stack_frame_with_id)
self._EnsureTimestampAdded(debug_event)
_pywrap_debug_events_writer.WriteStackFrameWithId(self._dump_root,
                                                  debug_event)
