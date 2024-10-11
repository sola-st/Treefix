# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
"""Evaluates a symbolic tensor as a constant.

  Args:
    tensor: a symbolic Tensor.

  Returns:
    ndarray if the evaluation succeeds, or None if it fails.
  """
# pylint: disable=protected-access
with tensor.graph._c_graph.get() as c_graph:
    exit(c_api.TF_TryEvaluateConstant_wrapper(c_graph, tensor._as_tf_output()))
