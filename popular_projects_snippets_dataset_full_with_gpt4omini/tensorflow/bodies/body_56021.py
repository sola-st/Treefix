# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe.py
"""Preserve the control flow context for the given tensor.

  Sets the graph context to the tensor's context so that side effect ops are
  added under the same context.

  This is needed when subscribing to tensors defined within a conditional
  block or a while loop. In these cases we need that the side-effect ops
  are created within the same control flow context as that of the tensor
  they are attached to.

  Args:
    tensor: tensor whose context should be preserved.

  Yields:
    None
  """

# pylint: disable=protected-access
context = tensor.op._get_control_flow_context()
# pylint: enable=protected-access
if context:
    context.Enter()
try:
    exit()
finally:
    if context:
        context.Exit()
