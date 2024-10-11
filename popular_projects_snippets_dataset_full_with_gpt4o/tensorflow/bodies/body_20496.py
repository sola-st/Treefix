# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Pad all input tensors given padded_shapes.

  The real shape tensors will be concatenated with the padded original inputs.

  Args:
    inputs: The original inputs.
    padded_shapes: A list of padded shapes for each input. If an entry is None,
      no padding is performed.
    padding_spec: An enum specified by `tpu.PaddingSpec`. This describes the
      padding policy when the `inputs` to `tf.tpu.replicate` is dynamic.
      One usage is to enable automatic bucketizing on the inputs by setting the
      value to `tpu.PaddingSpec.POWER_OF_TWO`, which can help to reduce the
      recompilation in the XLA side.

  Returns:
    The padded inputs and a PaddingMap list which maps the padded input
    dimension to the real shape argument index.
  """
# maximum_static_shapes[idx][i] indicates the maximum static size of ith
# dimension of the idx input among all the replicas.
maximum_static_shapes = []
# need_padding[idx][i] indicates whether the ith dimension of the idx input
# needs padding.
need_padding = []
input_shape_tensors = []
for core_idx, inputs_per_core in enumerate(inputs):
    for idx, input_tensor in enumerate(inputs_per_core):
        input_shape = input_tensor.get_shape().as_list()
        if core_idx == 0:
            input_shape_tensors.append([])
            maximum_static_shapes.append(input_shape)
            need_padding.append(np.full_like(input_shape, False, dtype=bool))
        else:
            for i, s in enumerate(input_shape):
                if s is None or s != maximum_static_shapes[idx][i]:
                    need_padding[idx][i] = True
            maximum_static_shapes[idx] = max(input_shape,
                                             maximum_static_shapes[idx])

        # Append _POST_DEVICE_REWRITE_ATTR attributes to the real shape ops.
        real_input_shape = array_ops.shape(input_tensor)
        real_input_shape.op._set_attr(  # pylint: disable=protected-access
            _POST_DEVICE_REWRITE_ATTR,
            attr_value_pb2.AttrValue(b=True))
        input_shape_tensors[idx].append(real_input_shape)

maximum_shapes = []
for shapes_per_input in input_shape_tensors:
    maximum_shapes.append(
        math_ops.reduce_max(array_ops.stack(shapes_per_input), axis=0))

padded_inputs = []
real_shapes = []
padding_maps = []
for core_idx, inputs_per_core in enumerate(inputs):
    padded_inputs.append([])
    real_shapes.append([])
    real_shape_idx = len(inputs_per_core) - 1
    for idx, input_tensor in enumerate(inputs_per_core):
        input_shape_tensor = input_shape_tensors[idx][core_idx]
        input_shape = input_tensor.get_shape().as_list()
        padded_shape = padded_shapes[idx]

        # If we have no padded_shape, then skip padding.
        if any(need_padding[idx]) and padded_shape is not None:
            for i, s in enumerate(input_shape):
                if need_padding[idx][i]:
                    if core_idx == 0:
                        real_shape_idx += 1
                        padding_map = dynamic_padding.PaddingMap()
                        padding_map.arg_index = idx
                        padding_map.shape_index = i
                        padding_map.padding_arg_index = real_shape_idx
                        padding_maps.append(padding_map)
                    real_shapes[core_idx].append(
                        math_ops.cast(input_shape_tensor[i], dtypes.int32))

            paddings = []
            for i, s in enumerate(padded_shape.dims):
                if need_padding[idx][i]:
                    # The minimum padded dimension size is 2 as XLA doesn't support size
                    # 1 dynamic size.
                    minimum_dynamic_dim_size = 2
                    if s.value is not None:
                        # Pad to the given maximum value.
                        max_dim_size = max(s.value, minimum_dynamic_dim_size)
                    else:
                        # If maximum value is not given, then pad to the maximum dimension
                        # among all the cores.
                        max_dim_size = math_ops.maximum(maximum_shapes[idx][i],
                                                        minimum_dynamic_dim_size)
                        if padding_spec == PaddingSpec.POWER_OF_TWO:
                            max_dim_size = _ceil_to_pow_of_n(max_dim_size, 2)
            # Pad to the given maximum value.
                    padding = [0, max_dim_size - input_shape_tensor[i]]
                else:
                    padding = [0, 0]
                paddings.append(padding)

            if input_tensor.get_shape().is_fully_defined():
                # TODO(rxsang): This is a hack to make sure padded_input has dynamic
                # shapes, so any tf.size/tf.shape op performed on it won't be constant
                # folded. Do we have better ways to do it?
                padded_input = control_flow_ops.cond(
                    array_ops.constant(True),
                    lambda: array_ops.pad(input_tensor, paddings),  # pylint: disable=cell-var-from-loop
                    lambda: input_tensor)
            else:
                padded_input = array_ops.pad(input_tensor, paddings)

            # Append _POST_DEVICE_REWRITE_ATTR attributes to all padded inputs.
            padded_input.op._set_attr(  # pylint: disable=protected-access
                _POST_DEVICE_REWRITE_ATTR,
                attr_value_pb2.AttrValue(b=True))

            padded_inputs[core_idx].append(padded_input)
        else:
            padded_inputs[core_idx].append(input_tensor)

num_replicas = len(padded_inputs)
for i in range(num_replicas):
    padded_inputs[i].extend(real_shapes[i])

exit((padded_inputs, padding_maps))
