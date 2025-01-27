# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer.py
"""Write a SourceFile proto with the writer.

    Args:
      source_file: A SourceFile proto, describing the content of a source file
        involved in the execution of the debugged TensorFlow program.
    """
# TODO(cais): Explore performance optimization that avoids memcpy.
debug_event = debug_event_pb2.DebugEvent(source_file=source_file)
self._EnsureTimestampAdded(debug_event)
_pywrap_debug_events_writer.WriteSourceFile(self._dump_root, debug_event)
