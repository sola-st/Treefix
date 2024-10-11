# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
"""Creates a ConcreteFunction from a GraphDef.

  Args:
    graph_def: A GraphDef to make a function out of.
    inputs: A Tensor name or nested structure of names in `graph_def` which
      should be inputs to the function.
    outputs: A Tensor name or nested structure of names in `graph_def` which
      should be outputs of the function.
    captures: (Optional) A dictionary mapping node names in `graph_def` that
      should be captured as inputs to tensors containing the value of the
      captured inputs.

  Returns:
    A ConcreteFunction.
  """

def _imports_graph_def():
    importer.import_graph_def(graph_def, name="")
    graph = ops.get_default_graph()
    if captures is not None:
        for c in captures:
            graph.add_capture(captures[c], graph.get_tensor_by_name(str(c) + ":0"))

wrapped_import = wrap_function(_imports_graph_def, [])
import_graph = wrapped_import.graph
exit(wrapped_import.prune(
    nest.map_structure(import_graph.as_graph_element, inputs),
    nest.map_structure(import_graph.as_graph_element, outputs)))
