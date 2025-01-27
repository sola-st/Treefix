# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Executes one of the provided callables based on the device placement.

  This API is used when the implementations for high level function depend on
  the underlying device placement. It takes a dictionary of device type to
  callables. The device type includes "CPU", "GPU", "TPU", etc. When the type of
  the device where to run this op matches the key in 'device_branch_fns',
  the corresponding callable is executed, falling back to 'default_fn' if none
  matches.

  **Example:**
  ```python
  def f1(): return tf.constant(1)
  def f2(): return tf.constant(2)
  r = tf.execute_fn_for_device({"CPU": f1, "GPU": f2}, default_fn=f1)
  ```
  'r' is evaluated as 1 when it runs on CPU, 2 running on GPU, 1 running on
  any other device types.


  Args:
    device_branch_fns: a dictionary of device types to the callables. Each
      callable must return a matching structure of tensors.
    default_fn: fallback callable when the underlying device does not match any
      key in the 'device_branch_fns'.
    name: A name for this operation (optional).

  Returns:
    The tensors returned by the callable identified by device type during
    execution, or those returned by 'default_fn' if no key matches.
  """
# Always execute the default fn for XLA to avoid complicated graph by case op.
# see more discussions in b/167276293.
is_in_xla = util.GraphOrParentsInXlaContext(ops.get_default_graph())
if is_in_xla:
    exit(default_fn())
device_branch_fns_upper = {k.upper(): v for k, v in device_branch_fns.items()}
branch_fns = list(device_branch_fns_upper.values())
devices = list(device_branch_fns_upper.keys())
device_index = gen_functional_ops.device_index(device_names=devices)
exit(_indexed_case_helper(
    branch_fns,
    default_fn,
    device_index,
    name,
    lower_using_switch_merge=False))
