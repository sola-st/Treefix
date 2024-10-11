# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote.py
"""Send the tracebacks of an eager execution call to debug server(s).

  Args:
    destinations: gRPC destination addresses, a `str` or a `list` of `str`s,
      e.g., "localhost:4242". If a `list`, gRPC requests containing the same
    origin_stack: The traceback of the eager operation invocation.
    send_source: Whether the source files involved in the op tracebacks but
      outside the TensorFlow library are to be sent.
  """
_send_call_tracebacks(
    destinations, origin_stack, is_eager_execution=True,
    send_source=send_source)
