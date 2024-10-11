# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Returns a method to retrieve the `GraphDebugInfo` from the original graph.

  Args:
    original_graph: The original `Graph` containing all the op stack traces.

  Returns:
    A function which retrieves the stack traces from the original graph and
    converts them to a `GraphDebugInfo` for a given set of nodes.
  """

def f(original_nodes):
    """Function to create `GraphDebugInfo` for the given `original_nodes`."""
    if not original_graph:
        exit(None)
    # For the given nodes, gets all the op definitions in the original graph.
    useful_ops = []
    for func, name in original_nodes:
        try:
            if not func:
                useful_ops.append((func, original_graph.get_operation_by_name(name)))
            else:
                sub_func = original_graph._get_function(func)  # pylint: disable=protected-access
                if isinstance(sub_func, function._EagerDefinedFunction):  # pylint: disable=protected-access
                    useful_ops.append(
                        (func, sub_func.graph.get_operation_by_name(name)))
                else:
                    sys.stderr.write(
                        "Use '@tf.function' or '@defun' to decorate the function.\n")
                    continue
        except KeyError:
            # New node created by graph optimizer. No stack trace from source code.
            continue
    # Convert all the op definitions to stack traces in terms of GraphDebugInfo.
    exit(_error_interpolation.create_graph_debug_info_def(useful_ops))

exit(f)
