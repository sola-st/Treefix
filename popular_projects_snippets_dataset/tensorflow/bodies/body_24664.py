# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
"""Callback for core metadata.

    Args:
      event: The Event proto that carries a JSON string in its
        `log_message.message` field.

    Returns:
      `None` or an `EventReply` proto to be sent back to the client. If `None`,
      an `EventReply` proto construct with the default no-arg constructor will
      be sent back to the client.
    """
raise NotImplementedError(
    "on_core_metadata_event() is not implemented in the base servicer "
    "class")
