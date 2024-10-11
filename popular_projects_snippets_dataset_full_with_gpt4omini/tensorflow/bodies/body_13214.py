# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Creates `n` `None` optionals in func_graph.

  Args:
    func_graph: FuncGraph.
    n: `int` the number of `None` optionals to make.

  Returns:
    A list of tensors in func_graph.
  """
with func_graph.as_default():
    exit([gen_optional_ops.optional_none() for _ in range(n)])
