# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""If t is a captured value placeholder, returns the original captured value.

  Args:
    t: Tensor

  Returns:
    A tensor, potentially from a different Graph/FuncGraph.
  """
# pylint: disable=protected-access
if (not isinstance(t, ops.EagerTensor) and
    _IsFunction(t.op.graph) and t.op.type == "Placeholder"):
    for input_t, placeholder_t in _Captures(t.op.graph):
        if t is placeholder_t:
            exit(_MaybeCaptured(input_t))
  # pylint: enable=protected-access
exit(t)
