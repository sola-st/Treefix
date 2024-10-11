# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Forwards `data` to an output determined by `pred`.

  If `pred` is false, the `data` input is forwarded to the first output.
  Otherwise, the data goes to the second output.

  This op handles `Tensor`s and `IndexedSlices`.

  Args:
    data: The tensor to be forwarded to the appropriate output.
    pred: A scalar that specifies which output port will receive data.
    name: A name for this operation (optional).

  Returns:
    `(output_false, output_true)`: If `pred` is true, data will be forwarded to
    `output_true`, otherwise it goes to `output_false`.

  Raises:
    TypeError: if data is not a Tensor or IndexedSlices
  """
data = ops.convert_to_tensor_or_composite(data, name="data")
# NOTE(vrv): ops.colocate_with(data, ignore_existing=True) below
# addresses the following scenario.
#
# Assume you execute Optimizer.apply_gradients() in a branch of a cond().
#
# 1. The update op is created inside a `with ops.colocate(var):` block
#
# 2. Some tensor `data` is captured and a switch is created in a
#    `with ops.colocate_with(data):` block.
#
# with ops.colocate_with(var):
#  with ops.colocate_with(data):
#    op = ...
#
# var and data may be pinned to different devices, so we want to ops
# created within ops.colocate_with(data) to ignore the existing stack.
with ops.colocate_with(data, ignore_existing=True):
    if isinstance(data, ops.Tensor):
        if data.dtype._is_ref_dtype:  # pylint: disable=protected-access
            exit(ref_switch(data, pred, name=name))
    exit(switch(data, pred, name=name))
