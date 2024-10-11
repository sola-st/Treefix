# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""A callback to be called on creation of Functions.

    Used to establish a join between function name and graph (context) ID.

    Args:
      function: The just-created Function.
      name: Name of the function.
      graph: FuncGraph, the graph containing the operations in the function.
      inputs: the tensors in the graph to be used as inputs to the function
      outputs: the tensors in the graph which will be outputs from the function
    """
del name, inputs, outputs

graph_id = self._get_context_id(graph)
with self._context_lock:
    # NOTE(cais): We currently store the function (_EagerDefinedFunction)
    # as keys of this dict, because weakrefs to them sometimes become
    # unreferenceable by the time the op callback is called. This approach
    # may cause memory leaks due to the holding of the functions. If that's
    # the case, calling `tf.debugging.disable_dump_debug_info()` should
    # cause GC of this object and this dict.
    self._function_to_graph_id[function] = graph_id
