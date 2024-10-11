# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Validates non-flat outputs, add backs device assignments and other attrs.

  Args:
    outputs: Output from `computation` inside `tpu.rewrite`.
    need_spmd_partitioning: Whether XLA SPMD partitioning is needed.

  Returns:
    - Tensors extracted from outputs.
    - An empty Operations list because Operations are not allowed in non-flat
      outputs.
    - A pack template for use with nest.pack_sequence_as to pack the tensors.
  """

# Flatten output items.
flat_outputs = nest.flatten(outputs, expand_composites=True)

# Convert all non-None non-Operation outputs to Tensors.
for i, o in enumerate(flat_outputs):
    if o is None:
        flat_outputs[i] = None
        continue

    if isinstance(o, ops.Operation):
        raise ValueError(
            "tpu.rewrite does not support Operation as return value in non-flat "
            "output structure. You can set returned Operations as control "
            "dependencies of returned Tensors so Operations are triggered when "
            f'Tensors are evaluated. Operation found: "{o.name}"')

    try:
        o = ops.convert_to_tensor(o)
    except Exception as e:
        raise ValueError(
            "TPU function return values must all either be Operations or "
            f'convertible to Tensors. Got error: "{e}"')

    # Wraps outputs in Identity ops. Otherwise a replicated input copied
    # straight to an output would bypass the replicate(). This would be bad
    # because the TPUReplicatedInput/TPUReplicatedOutput operator would not
    # be rewritten away, leading to a runtime error.
    # TODO(phawkins): extend the rewrite to elide these nodes instead.
    if need_spmd_partitioning:
        o = array_ops.identity(o)
        # pylint: disable=protected-access
        o.op._set_attr("_tpu_output_identity", attr_value_pb2.AttrValue(b=True))
        # pylint: enable=protected-access
        flat_outputs[i] = array_ops.identity(o)
    else:
        with ops.device(o.device if o.device else core(0)):
            o = array_ops.identity(o)
            # pylint: disable=protected-access
            o.op._set_attr("_tpu_output_identity", attr_value_pb2.AttrValue(b=True))
            # pylint: enable=protected-access
            flat_outputs[i] = array_ops.identity(o)

  # All flat_outputs are Tensors, and no Operations.
exit((flat_outputs, [], outputs))
