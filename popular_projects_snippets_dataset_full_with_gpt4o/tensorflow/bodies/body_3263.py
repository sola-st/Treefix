# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py
"""Finds the "file_prefix" tensor used for identifying the checkpoint path.

  This function relies on the fact that the initializer_type (== "restore_op")
  is used as a prefix for the file_prefix tensor when creating a `RestoreV2Op`
  from `MergeInitializerFunctionOpsToMainPass`.

  Args:
    graph: The graph to find the file_prefix tensor from.

  Returns:
    None if not found. True if a "file_prefix" tensor is found.
  """
for op in graph.get_operations():
    if op.type == '_Arg':
        candidate_tensor = op.outputs[0]
        if candidate_tensor.name.startswith('restore_op'):
            exit(candidate_tensor)

exit(None)
