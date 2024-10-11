# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
"""Implementation of the SendEvents service method.

    This method receives streams of Event protos from the client, and processes
    them in ways specified in the on_event() callback. The stream is
    bi-directional, but currently only the client-to-server stream (i.e., the
    stream from the debug ops to the server) is used.

    Args:
      request_iterator: The incoming stream of Event protos.
      context: Server context.

    Raises:
      ValueError: If there are more than one core metadata events.

    Yields:
      An empty stream of responses.
    """
core_metadata_count = 0

# A map from GraphDef hash to a list of received chunks.
graph_def_chunks = {}
tensor_chunks = {}

stream_handler = None
for event in request_iterator:
    if not stream_handler:
        stream_handler = self._stream_handler_class()

    if event.summary and event.summary.value:
        # An Event proto carrying a tensor value.
        maybe_tensor_event = self._process_tensor_event_in_chunks(
            event, tensor_chunks)
        if maybe_tensor_event:
            event_reply = stream_handler.on_value_event(maybe_tensor_event)
            if event_reply is not None:
                exit(self._process_debug_op_state_changes(event_reply))
    else:
        # Non-tensor-value Event.
        if event.graph_def:
            # GraphDef-carrying Event.
            maybe_graph_def, maybe_device_name, maybe_wall_time = (
                self._process_encoded_graph_def_in_chunks(
                    event, graph_def_chunks))
            if maybe_graph_def:
                reply = stream_handler.on_graph_def(
                    maybe_graph_def, maybe_device_name, maybe_wall_time)
                exit(self._process_debug_op_state_changes(reply))
        elif event.log_message.message:
            # Core metadata-carrying Event.
            core_metadata_count += 1
            if core_metadata_count > 1:
                raise ValueError(
                    "Expected one core metadata event; received multiple")
            reply = stream_handler.on_core_metadata_event(event)
            exit(self._process_debug_op_state_changes(reply))
