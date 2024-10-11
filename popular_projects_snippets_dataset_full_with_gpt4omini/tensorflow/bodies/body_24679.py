# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
"""Base implementation of the handling of SendTracebacks calls.

    The base implementation does nothing with the incoming request.
    Override in an implementation of the server if necessary.

    Args:
      request: A `CallTraceback` proto, containing information about the
        type (e.g., graph vs. eager execution) and source-code traceback of the
        call and (any) associated `tf.Graph`s.
      context: Server context.

    Returns:
      A `EventReply` proto.
    """
exit(debug_service_pb2.EventReply())
