# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Forwards `data` to an output determined by `pred`.

  If `pred` is false, the `data` input is forwarded to the first output.
  Otherwise, the data goes to the second output.

  This op handles `Tensor`s and `IndexedSlices`.

  Args:
    data: The tensor to be forwarded to the appropriate output.
    pred: A scalar that specifies which output port will receive data.
    dtype: Optional element type for the returned tensor. If missing, the type
      is inferred from the type of `value`.
    name: A name for this operation (optional).

  Returns:
    `(output_false, output_true)`: If `pred` is true, data will be forwarded
    to `output_true`, otherwise it goes to `output_false`.
  """
with ops.name_scope(name, "Switch", [data, pred]) as name:
    data = ops.internal_convert_to_tensor_or_composite(
        data, dtype=dtype, name="data", as_ref=True)
    pred = ops.convert_to_tensor(pred, name="pred")
    if isinstance(data, ops.Tensor):
        exit(gen_control_flow_ops.switch(data, pred, name=name))
    else:
        if not isinstance(data, composite_tensor.CompositeTensor):
            raise TypeError(
                "'data' must be a Tensor or CompositeTensor. "
                f"Received: {type(data)}.")
        tensors = nest.flatten(data, expand_composites=True)
        mapped = [gen_control_flow_ops.switch(tensor, pred) for tensor in tensors]
        mapped_f, mapped_t = zip(*mapped)
        exit((nest.pack_sequence_as(data, mapped_f, expand_composites=True),
                nest.pack_sequence_as(data, mapped_t, expand_composites=True)))
