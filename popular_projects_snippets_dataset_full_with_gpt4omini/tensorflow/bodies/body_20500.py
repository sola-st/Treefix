# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Validates non-flat outputs, add backs device assignments and other attrs.

  Args:
    outputs: Output from `computation` inside `tpu.rewrite`.
    need_spmd_partitioning: Whether XLA SPMD partitioning is needed.

  Returns:
    - Tensors extracted from outputs.
    - Operations extracted from outputs.
    - A pack template for use with nest.pack_sequence_as to pack the tensors.
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

# For legacy / backwards compatibility reasons we return a list for "flat"
# output values (even if the user's flat return value was a different type or
# even just a scalar value) so use nest.flatten to compute a flat list pack
# template.
pack_template = nest.flatten(outputs, expand_composites=False)

# Even though outputs is already "flat", we flatten any composites so their
# component tensors can be tagged and replicated. The pack_template will be
# used by the caller to repack the composite tensors.
outputs = nest.flatten(outputs, expand_composites=True)

# Append `no_op` here so that fetching any return value of this function
# will trigger TPUExecute node.
outputs += (control_flow_ops.no_op(),)

maybe_convert = lambda x: None if x is None else ops.convert_to_tensor(x)
try:
    if need_spmd_partitioning:
        outputs = [
            o if isinstance(o, ops.Operation) else maybe_convert(o)
            for o in outputs
        ]
    else:
        with ops.device(core(0)):
            outputs = [
                o if isinstance(o, ops.Operation) else maybe_convert(o)
                for o in outputs
            ]
except Exception as e:
    raise ValueError(
        "TPU function return values must all either be Operations or "
        f"convertible to Tensors. Got error: {e}")

# Separates the returned Operations and Tensors.
output_operations = [o for o in outputs if isinstance(o, ops.Operation)]
output_tensors = [o for o in outputs if not isinstance(o, ops.Operation)]

if outputs != output_tensors + output_operations:
    raise ValueError(
        "TPU functions must return zero-or more Tensor values followed by "
        "zero or more Operations.")

# Trim operations off the end of the pack template. output_operations has 1
# extra element due to the no-op that is added.
if len(output_operations) > 1:
    pack_template = pack_template[:1 - len(output_operations)]

# Wraps outputs in Identity ops. Otherwise a replicated input copied
# straight to an output would bypass the replicate(). This would be bad
# because the TPUReplicatedInput/TPUReplicatedOutput operator would not
# be rewritten away, leading to a runtime error.
# TODO(phawkins): extend the rewrite to elide these nodes instead.
new_output_tensors = []
for t in output_tensors:
    if t is None:
        new_output_tensors.append(None)
    elif need_spmd_partitioning:
        o = array_ops.identity(t)
        # pylint: disable=protected-access
        o.op._set_attr("_tpu_output_identity", attr_value_pb2.AttrValue(b=True))
        # pylint: enable=protected-access
        new_output_tensors.append(o)
    else:
        with ops.device(t.device if t.device else core(0)):
            o = array_ops.identity(t)
            # pylint: disable=protected-access
            o.op._set_attr("_tpu_output_identity", attr_value_pb2.AttrValue(b=True))
            # pylint: enable=protected-access
            new_output_tensors.append(o)
exit((new_output_tensors, output_operations, pack_template))
