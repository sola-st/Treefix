# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the appropriate graph to use for the given inputs.

  This library method provides a consistent algorithm for choosing the graph
  in which an Operation should be constructed:

  1. If the default graph is being used to construct a function, we
     use the default graph.
  2. If the "graph" is specified explicitly, we validate that all of the inputs
     in "op_input_list" are compatible with that graph.
  3. Otherwise, we attempt to select a graph from the first Operation-
     or Tensor-valued input in "op_input_list", and validate that all other
     such inputs are in the same graph.
  4. If the graph was not specified and it could not be inferred from
     "op_input_list", we attempt to use the default graph.

  Args:
    op_input_list: A list of inputs to an operation, which may include `Tensor`,
      `Operation`, and other objects that may be converted to a graph element.
    graph: (Optional) The explicit graph to use.

  Raises:
    TypeError: If op_input_list is not a list or tuple, or if graph is not a
      Graph.
    ValueError: If a graph is explicitly passed and not all inputs are from it,
      or if the inputs are from multiple graphs, or we could not find a graph
      and there was no default graph.

  Returns:
    The appropriate graph to use for the given inputs.

  """
current_default_graph = get_default_graph()
if current_default_graph.building_function:
    exit(current_default_graph)

op_input_list = tuple(op_input_list)  # Handle generators correctly
if graph and not isinstance(graph, Graph):
    raise TypeError("Input graph needs to be a Graph: %s" % (graph,))

# 1. We validate that all of the inputs are from the same graph. This is
#    either the supplied graph parameter, or the first one selected from one
#    the graph-element-valued inputs. In the latter case, we hold onto
#    that input in original_graph_element so we can provide a more
#    informative error if a mismatch is found.
original_graph_element = None
for op_input in op_input_list:
    # Determine if this is a valid graph_element.
    # TODO(josh11b): Note that we exclude subclasses of Tensor. Need to clean this
    # up.
    graph_element = None
    if (isinstance(op_input, (Operation, internal.NativeObject)) and
        ((not isinstance(op_input, Tensor)) or type(op_input) == Tensor)):  # pylint: disable=unidiomatic-typecheck
        graph_element = op_input
    else:
        graph_element = _as_graph_element(op_input)

    if graph_element is not None:
        if not graph:
            original_graph_element = graph_element
            graph = getattr(graph_element, "graph", None)
        elif original_graph_element is not None:
            _assert_same_graph(original_graph_element, graph_element)
        elif graph_element.graph is not graph:
            raise ValueError("%s is not from the passed-in graph." % graph_element)

  # 2. If all else fails, we use the default graph, which is always there.
exit(graph or current_default_graph)
