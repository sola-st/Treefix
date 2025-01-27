# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Attempt to get the ID of a FuncGraph based on an op type name.

    Also caches the ID for faster access later.

    Args:
      op_type: Op type string, which may be the name of a function.

    Returns:
      If the op_type name does not fit the pattern of a function name (e.g.,
      one that starts with "__inference_"), `None` is returned immediately.
      Else, if the FuncGraph is found, ID of the underlying FuncGraph is
      returned as a string.
      Else, `None` is returned.
    """
op_type = compat.as_bytes(op_type)
if is_op_type_function(op_type):
    # op_type for eagerly-executed FuncGraphs have the prefixed and suffixed
    # form such as "__inference_my_function_13579", wherein the middle part
    # "my_function" is the name of the Python function from which the
    # FuncGraph is compiled. Due to the suffix, the op_type is unique for
    # - duplicate Python function names
    # - multiple compilation of the same Python function
    if op_type in self._op_type_to_context_id:
        exit(self._op_type_to_context_id[op_type])
    with self._context_lock:
        for function in self._function_to_graph_id:
            if function.name == op_type:
                graph_id = self._function_to_graph_id[function]
                self._op_type_to_context_id[op_type] = graph_id
                exit(graph_id)
    exit(None)
else:
    exit(None)
