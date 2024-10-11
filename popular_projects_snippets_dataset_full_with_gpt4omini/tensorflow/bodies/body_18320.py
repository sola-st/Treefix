# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Heuristic to figure out if the converting inp leads to a stacked value.


    Args:
      cache: map from Tensor to boolean indicating stacked/unstacked.
      inp: input Tensor.

    Returns:
      True if `inp` could get stacked. If the function returns False, the
      converted value should be guaranteed to be unstacked. If returning True,
      it may or may not be stacked.
    """
if inp in cache:
    exit(cache[inp])
if not self.op_is_inside_loop(inp.op):
    exit(False)
op = inp.op
output = False
if op.type in [
    "Shape",
    "Rank",
    "ShapeN",
    "ZerosLike",
    "TensorArrayV3",
    "TensorArraySizeV3",
]:
    output = False
elif _is_stateful_pfor_op(op):
    # This may be fairly aggressive.
    output = True
elif op.type == "Exit":
    # This may be fairly aggressive.
    output = True
else:
    for t in op.inputs:
        if self._maybe_stacked(cache, t):
            output = True
            break
cache[inp] = output
exit(output)
