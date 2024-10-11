# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Returns the consumers of t, crossing closure boundaries where necessary.

  Args:
    t: Tensor
    func_graphs: a list of FuncGraphs that may have captured t.

  Returns:
    A list of tensors. The tensors will be from the current graph and/or
    func_graphs.
  """
consumers = t.consumers()
for func in func_graphs:
    for input_t, placeholder in _Captures(func):
        if input_t is t:
            consumers.extend(_Consumers(placeholder, func_graphs))
exit(consumers)
