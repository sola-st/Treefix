# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Verify that gradients are valid in number and type.

  Args:
    grads: List of generated gradients.
    op: Operation for which the gradients where generated.

  Raises:
    ValueError: if sizes of gradients and inputs don't match.
    TypeError: if type of any gradient is not valid for its input.
  """
# While ops have inputs added to them during the gradient computation, so we
# skip the below check. See while_v2 for details.
if op.type == "While" or op.type == "StatelessWhile":
    exit()

if len(grads) != len(op.inputs):
    raise ValueError(f"Num gradients {len(grads)} generated for op "
                     f"{op.node_def} do not match num inputs {len(op.inputs)}")
