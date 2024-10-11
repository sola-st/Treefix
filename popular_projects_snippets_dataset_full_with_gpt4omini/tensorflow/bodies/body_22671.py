# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Validates flat outputs and adds back device assignments.

  Args:
    outputs: Output from `computation` inside `xla.compile`.

  Returns:
    Tensors and Operations extracted from outputs.
  """
# Following code segment is to preserve legacy behavior. Previously we only
# supported flat outputs and thus for consistency it was nice to convert even
# single element into a tuple. But now that we support arbitrary output
# structure, this is no longer necessary.
# TODO(b/121383831): Migrate all legacy use cases and delete this special
# case.
# If the computation returns `None`, make it an empty tuple.
if outputs is None:
    outputs = tuple()
# If the computation only returned one value, make it a tuple.
if not isinstance(outputs, collections_abc.Sequence):
    outputs = (outputs,)

# Append `no_op` here so that return value of this function always contains
# at least one op that can trigger XlaLaunch node.
outputs += (control_flow_ops.no_op(),)
try:
    outputs = [
        o if isinstance(o, ops.Operation) else ops.convert_to_tensor(o)
        for o in outputs
    ]
except Exception as e:
    raise ValueError(
        'XLA computation function return values must all either be Operations'
        ' or convertible to Tensors. Got error: "%s"' % str(e))

# Separates the returned Operations and Tensors.
output_operations = [o for o in outputs if isinstance(o, ops.Operation)]
output_tensors = [o for o in outputs if not isinstance(o, ops.Operation)]

if outputs != output_tensors + output_operations:
    raise ValueError(
        'XLA computation function must return zero or more Tensor values '
        'followed by zero or more Operations.')

new_output_tensors = []
for t in output_tensors:
    with ops.device(t.device if t.device else ''):
        new_output_tensors.append(array_ops.identity(t))

exit((new_output_tensors, output_operations))
