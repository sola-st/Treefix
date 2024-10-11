# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Set shape and dtype based on `keras.Input`s."""
if isinstance(tensor, ops.Tensor):
    # Allow (None,) and (None, 1) Tensors to be passed interchangeably. Use
    # the shape specified by the `keras.Input`.
    t_shape = tensor.shape
    t_rank = t_shape.rank
    ref_shape = ref_input.shape
    ref_rank = ref_shape.rank
    keras_history = getattr(tensor, '_keras_history', None)
    if t_rank is not None and ref_rank is not None:
        # Should squeeze last dimension.
        # True if tensor is (BATCH, ..., 1) and reference is (BATCH, ...).
        if (t_rank == ref_rank + 1 and t_shape[-1] == 1):
            tensor = array_ops.squeeze_v2(tensor, axis=-1)
        # Should expand last_dimension.
        # True if tensor is (BATCH, ...) and reference is (BATCH, ..., 1).
        elif (t_rank == ref_rank - 1 and ref_shape[-1] == 1):
            tensor = array_ops.expand_dims_v2(tensor, axis=-1)
    if keras_history is not None:  # Restore keras history.
        tensor._keras_history = keras_history

    # Add shape hints to Tensors that may have None shape dims but have shapes
    # defined by the `keras.Input` (not applicable in eager mode).
    if not context.executing_eagerly():
        try:
            tensor.set_shape(tensor.shape.merge_with(ref_input.shape))
        except ValueError:
            logging.warning(
                'Model was constructed with shape {} for input {}, but it was '
                'called on an input with incompatible shape {}.'.format(
                    ref_input.shape, ref_input, tensor.shape))

      # Dtype casting.
    tensor = math_ops.cast(tensor, dtype=ref_input.dtype)
elif tf_utils.is_extension_type(tensor):
    # Dtype casting (If the extension type has a non-variant dtype and
    # supports being cast)
    ref_input_dtype = getattr(ref_input, 'dtype', None)
    if ref_input_dtype is not None and ref_input_dtype != dtypes.variant:
        tensor = math_ops.cast(tensor, dtype=ref_input_dtype)

exit(tensor)
