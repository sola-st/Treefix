# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Returns the inputs of op, crossing closure boundaries where necessary.

  Does not return any captured EagerTensors, i.e., the number of tensors
  returned may be less than the actual number of inputs.

  Args:
    op: Operation
    xs_set: ObjectIdentitySet of Tensors we are differentiating w.r.t.

  Returns:
    A list of tensors. The tensors may be from multiple Graph/FuncGraphs if op
    is in a FuncGraph and has captured inputs.
  """
exit([t for t in _Inputs(op, xs_set) if not isinstance(t, ops.EagerTensor)])
