# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote.py
"""Send the tracebacks of a graph execution call to debug server(s).

  Args:
    destinations: gRPC destination addresses, a `str` or a `list` of `str`s,
      e.g., "localhost:4242". If a `list`, gRPC requests containing the same
      `CallTraceback` proto payload will be sent to all the destinations.
    run_key: A string describing the feeds, fetches (and targets) names of the
      `tf.Session.run` call.
    origin_stack: The traceback of the `tf.Session.run()` invocation.
    graph: A Python `tf.Graph` object (i.e., *not* a `tf.compat.v1.GraphDef`),
      which contains op tracebacks.
    send_source: Whether the source files involved in the op tracebacks but
      outside the TensorFlow library are to be sent.
  """
_send_call_tracebacks(
    destinations, origin_stack, is_eager_execution=False, call_key=run_key,
    graph=graph, send_source=send_source)
