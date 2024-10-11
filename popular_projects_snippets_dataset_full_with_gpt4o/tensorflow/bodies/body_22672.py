# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Validates non-flat outputs and adds back device assignments.

  Args:
    outputs: Output from `computation` inside `xla.compile`.

  Returns:
    Tensors extracted from outputs and an empty list because Operations are not
    allowed in non-flat outputs..
  """
# Convert all non-Operation outputs to Tensors.
new_output_tensors = []
for o in nest.flatten(outputs):
    if isinstance(o, ops.Operation):
        raise ValueError(
            'xla.compile does not support Operation as return value in non-flat '
            'output structure. You can set returned Operations as control '
            'dependencies of returned Tensors so Operations are triggered when '
            'Tensors are evaluated. Operation found: "%s"' % o.name)

    try:
        o = ops.convert_to_tensor(o)
    except Exception as e:
        raise ValueError(
            'XLA computation function return values must all either be '
            'Operations or convertible to Tensors. Got error: "%s"' % str(e))

    # Makes sure even pass-through inputs/outputs are touched in compile
    # context by creating an Identity node inside compile context.
    with ops.device(o.device if o.device else ''):
        new_output_tensors.append(array_ops.identity(o))

exit((new_output_tensors, []))
