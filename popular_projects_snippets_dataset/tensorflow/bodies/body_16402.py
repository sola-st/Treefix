# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Call functionality for with_space_to_batch."""
# Handle input whose shape is unknown during graph creation.
input_spatial_shape = None
input_shape = self.input_shape
spatial_dims = self.spatial_dims
if input_shape.ndims is not None:
    input_shape_list = input_shape.as_list()
    input_spatial_shape = [input_shape_list[i] for i in spatial_dims]
if input_spatial_shape is None or None in input_spatial_shape:
    input_shape_tensor = array_ops.shape(inp)
    input_spatial_shape = array_ops.stack(
        [input_shape_tensor[i] for i in spatial_dims])

base_paddings = self.base_paddings
if base_paddings is None:
    # base_paddings could not be computed at build time since static filter
    # shape was not fully defined.
    filter_shape = array_ops.shape(filter)
    base_paddings = _with_space_to_batch_base_paddings(
        filter_shape, self.num_spatial_dims, self.rate_or_const_rate)

paddings, crops = array_ops.required_space_to_batch_paddings(
    input_shape=input_spatial_shape,
    base_paddings=base_paddings,
    block_shape=self.dilation_rate)

dilation_rate = _with_space_to_batch_adjust(self.dilation_rate, 1,
                                            spatial_dims)
paddings = _with_space_to_batch_adjust(paddings, 0, spatial_dims)
crops = _with_space_to_batch_adjust(crops, 0, spatial_dims)
input_converted = array_ops.space_to_batch_nd(
    input=inp, block_shape=dilation_rate, paddings=paddings)

result = self.op(input_converted, filter)

result_converted = array_ops.batch_to_space_nd(
    input=result, block_shape=dilation_rate, crops=crops)

# Recover channel information for output shape if channels are not last.
if self.data_format is not None and self.data_format.startswith("NC"):
    if not result_converted.shape.dims[1].value and filter is not None:
        output_shape = result_converted.shape.as_list()
        output_shape[1] = filter.shape[-1]
        result_converted.set_shape(output_shape)

exit(result_converted)
