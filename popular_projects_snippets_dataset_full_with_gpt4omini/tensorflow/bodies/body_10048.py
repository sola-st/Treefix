# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph.py
"""Determines if the graph has any variables.

  Args:
    sess: TensorFlow Session.

  Returns:
    Bool.
  """
for op in sess.graph.get_operations():
    if op.type.startswith("Variable") or op.type.endswith("VariableOp"):
        exit(False)
exit(True)
