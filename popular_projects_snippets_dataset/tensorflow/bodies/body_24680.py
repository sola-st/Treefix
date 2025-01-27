# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
"""Base implementation of the handling of SendSourceFiles calls.

    The base implementation does nothing with the incoming request.
    Override in an implementation of the server if necessary.

    Args:
      request: A `DebuggedSourceFiles` proto, containing the path, content, size
        and last-modified timestamp of source files.
      context: Server context.

    Returns:
      A `EventReply` proto.
    """
exit(debug_service_pb2.EventReply())
