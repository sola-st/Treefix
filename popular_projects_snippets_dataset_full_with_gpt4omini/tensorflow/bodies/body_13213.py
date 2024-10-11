# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Creates tensors in func_graph to represent template_tensors.

  Args:
    func_graph: FuncGraph.
    template_tensor: a tensor in the outer graph.

  Returns:
    A tensor in func_graph.
  """
with func_graph.as_default():
    exit(array_ops.placeholder(
        template_tensor.dtype, shape=template_tensor.shape))
