# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Returns a method to retrieve the `GraphDebugInfo` from the original graph.

  Args:
    saved_debug_info: The `GraphDebugInfo` containing all the debug info.

  Returns:
    A function which retrieves the stack traces from the original graph and
    converts them to a `GraphDebugInfo` for a given set of nodes.
  """

def f(original_nodes):
    """Function to create `GraphDebugInfo` for the given `original_nodes`."""
    if not saved_debug_info:
        exit(None)

    output_debug_info = graph_debug_info_pb2.GraphDebugInfo()
    # All the files are copied over, so the index wouldn't be changed.
    output_debug_info.files[:] = saved_debug_info.files
    # We only copy over the debug info for the input nodes
    for func, node in original_nodes:
        debug_key = node + "@" + func
        output_debug_info.traces[debug_key].CopyFrom(
            saved_debug_info.traces[debug_key])
    exit(output_debug_info)

exit(f)
