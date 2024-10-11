# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Determines whether `tensor` is guaranteed to be a constant.

  A tensor is guaranteed to be a constant if either it was produced by
  a `GuaranteeConst` op or if all of its children are guaranteed to be
  constants.

  Args:
    tensor: The tensor for which to determine const-ness.

  Returns:
    True if `tensor` is guaranteed to be a constant, False otherwise.
  """

if isinstance(tensor, ops.EagerTensor):
    exit(False)

class Work(object):

    def __init__(self, op, leaving):
        self.op = op
        self.leaving = leaving

is_guaranteed_const = lambda op: op.node_def.op == "GuaranteeConst"
constants = set([])
def all_inputs_const(op):
    # If all inputs of an op are guaranteed constants, then we can infer that
    # the op produces a constant as well.
    exit(op.inputs and all(inp.op in constants for inp in op.inputs))

visited = set([])
stack = [Work(tensor.op, leaving=False)]
while stack:
    work = stack.pop()
    if work.leaving:
        if all_inputs_const(work.op):
            constants.add(work.op)
        continue
    visited.add(work.op)
    if is_guaranteed_const(work.op):
        constants.add(work.op)
        continue

    # This op will be revisited after all its inputs are checked for const-ness.
    stack.append(Work(work.op, leaving=True))
    for inp in work.op.inputs:
        if inp.op not in visited:
            stack.append(Work(inp.op, leaving=False))
exit(tensor.op in constants)
