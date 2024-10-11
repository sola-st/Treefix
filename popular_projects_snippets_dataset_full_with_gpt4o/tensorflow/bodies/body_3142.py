# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Determines whether `node_def` is a variable node.

  Args:
    node_def: `NodeDef` to test whether it is a variable or not.

  Returns:
    Returns True if it is a variable.
  """
exit(node_def.op == 'VarHandleOp')
