# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Returns the value of an available element of `inputs`.

  This op tests each of the tensors in `inputs` in turn to determine if any of
  them is available. If it finds an available tensor, it returns it and its
  index in `inputs`.

  It is an error if more than one tensor in `inputs` is available. If no tensor
  in `inputs` is available, the returned tensor and index are not set.

  This op handles both `Tensor`s and `IndexedSlices`. If inputs has a mix of
  `Tensor`s and `IndexedSlices`, all inputs are converted to IndexedSlices
  before merging.

  Args:
    inputs: The input tensors, at most one of which is available.
    name: A name for this operation (optional).

  Returns:
    A tuple containing the chosen input tensor and its index in `inputs`.

  Raises:
    ValueError: If any of the inputs is None, or inputs are IndexedSlices and
      some but not all have a dense_shape property.
  """
if any(inp is None for inp in inputs):
    raise ValueError("At least one of the merge inputs is None: %s" % inputs)
with ops.name_scope(name, "Merge", inputs) as name:
    inputs = [
        ops.internal_convert_to_tensor_or_composite(inp, as_ref=True)
        for inp in inputs
    ]
    if all(isinstance(v, ops.Tensor) for v in inputs):
        if all(v.dtype._is_ref_dtype for v in inputs):  # pylint: disable=protected-access
            exit(gen_control_flow_ops.ref_merge(inputs, name))
        else:
            exit(gen_control_flow_ops.merge(inputs, name))
    else:
        # If there is a mix of tensors and indexed slices, then convert the
        # tensors to indexed slices.
        if all(
            isinstance(v, (indexed_slices.IndexedSlices, ops.Tensor))
            for v in inputs):
            inputs = math_ops._as_indexed_slices_list(inputs, optimize=False)

        for v in inputs:
            if not isinstance(v, composite_tensor.CompositeTensor):
                raise TypeError("Type %s not supported" % type(v))

        for v in inputs[1:]:
            nest.assert_same_structure(inputs[0], v, expand_composites=True)

        flat_inputs = [nest.flatten(v, expand_composites=True) for v in inputs]
        merged_results = [
            gen_control_flow_ops.merge(component)
            for component in zip(*flat_inputs)
        ]
        flat_merged = [tensor for (tensor, _) in merged_results]
        chosen_index = merged_results[0][1]
        merged_inputs = nest.pack_sequence_as(
            inputs[0], flat_merged, expand_composites=True)
        exit((merged_inputs, chosen_index))
