# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
"""Callback for Event proto received through the gRPC stream.

    This Event proto carries a Tensor in its summary.value[0] field.

    Args:
      event: The Event proto from the stream to be processed.
    """
raise NotImplementedError(
    "on_value_event() is not implemented in the base servicer class")
