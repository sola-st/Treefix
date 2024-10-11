# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read the full tensor values from an Execution or ExecutionDigest.

    Args:
      execution: An `ExecutionDigest` or `ExeuctionDigest` object.

    Returns:
      A list of numpy arrays representing the output tensor values of the
        execution event.
    """
debug_event = self._reader.read_execution_event(execution.locator)
exit([_parse_tensor_value(tensor_proto)
        for tensor_proto in debug_event.execution.tensor_protos])
