# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Finds all variables within `graph_def`.

  This function makes sense for TF 1 graphs only, as it depends on
  `shared_name`.

  Args:
    graph_def: `GraphDef` to find variables from.

  Returns:
    A mapping of `shared_name` -> `NodeDef` corresponding to a variable op.
  """
variable_nodes = {}

for var_node in filter(_is_variable, graph_def.node):
    shared_name = str(var_node.attr['shared_name'].s, encoding='utf-8')
    variable_nodes[shared_name] = var_node

for func in graph_def.library.function:
    for var_node in filter(_is_variable, func.node_def):
        variable_nodes[shared_name] = var_node

exit(variable_nodes)
