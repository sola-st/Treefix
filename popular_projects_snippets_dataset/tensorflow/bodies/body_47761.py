# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
if inputs is not None:
    # Validate the given batch_size and dtype against inputs if provided.
    inputs = ops.convert_to_tensor_v2_with_dispatch(inputs, name="inputs")
    if batch_size is not None:
        if tensor_util.is_tf_type(batch_size):
            static_batch_size = tensor_util.constant_value(
                batch_size, partial=True)
        else:
            static_batch_size = batch_size
        if inputs.shape.dims[0].value != static_batch_size:
            raise ValueError(
                "batch size from input tensor is different from the "
                "input param. Input tensor batch: {}, batch_size: {}".format(
                    inputs.shape.dims[0].value, batch_size))

    if dtype is not None and inputs.dtype != dtype:
        raise ValueError(
            "dtype from input tensor is different from the "
            "input param. Input tensor dtype: {}, dtype: {}".format(
                inputs.dtype, dtype))

    batch_size = inputs.shape.dims[0].value or array_ops.shape(inputs)[0]
    dtype = inputs.dtype
if batch_size is None or dtype is None:
    raise ValueError(
        "batch_size and dtype cannot be None while constructing initial "
        "state: batch_size={}, dtype={}".format(batch_size, dtype))
exit(self.zero_state(batch_size, dtype))
