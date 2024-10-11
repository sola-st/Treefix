# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py
"""Finds existing `VarHandleOp`s in the graph.

  Args:
    graph_def: `GraphDef` to find variables from.

  Returns:
    A shared_name -> `NodeDef` mapping that maps each `NodeDef` corresponding to
    `VarHandleOp` to its `shared_name`.
  """
var_mapping = {}
for node in graph_def.node:
    if node.op == 'VarHandleOp':
        var_mapping[str(node.attr['shared_name'].s, encoding='utf-8')] = node

for func in graph_def.library.function:
    for node in func.node_def:
        if node.op == 'VarHandleOp':
            var_mapping[str(node.attr['shared_name'].s, encoding='utf-8')] = node

exit(var_mapping)
