# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Instantiates a placeholder tensor and returns it.

  Args:
      shape: Shape of the placeholder
          (integer tuple, may include `None` entries).
      ndim: Number of axes of the tensor.
          At least one of {`shape`, `ndim`} must be specified.
          If both are specified, `shape` is used.
      dtype: Placeholder type.
      sparse: Boolean, whether the placeholder should have a sparse type.
      name: Optional name string for the placeholder.
      ragged: Boolean, whether the placeholder should have a ragged type.
          In this case, values of 'None' in the 'shape' argument represent
          ragged dimensions. For more information about RaggedTensors, see this
          [guide](https://www.tensorflow.org/guide/ragged_tensors).

  Raises:
      ValueError: If called with sparse = True and ragged = True.

  Returns:
      Tensor instance (with Keras metadata included).

  Examples:


  >>> input_ph = tf.keras.backend.placeholder(shape=(2, 4, 5))
  >>> input_ph
  <KerasTensor: shape=(2, 4, 5) dtype=float32 (created by layer ...)>

  """
if sparse and ragged:
    raise ValueError(
        'Cannot set both sparse and ragged to True when creating a placeholder.'
    )
if dtype is None:
    dtype = floatx()
if not shape:
    if ndim:
        shape = (None,) * ndim
if ops.executing_eagerly_outside_functions():
    if sparse:
        spec = sparse_tensor.SparseTensorSpec(
            shape=shape, dtype=dtype)
    elif ragged:
        ragged_rank = 0
        for i in range(1, len(shape)):
            # Hacky because could be tensorshape or tuple maybe?
            # Or just tensorshape?
            if shape[i] is None or (
                hasattr(shape[i], 'value') and
                shape[i].value is None):
                ragged_rank = i
        spec = ragged_tensor.RaggedTensorSpec(
            shape=shape, dtype=dtype, ragged_rank=ragged_rank)
    else:
        spec = tensor_spec.TensorSpec(
            shape=shape, dtype=dtype, name=name)
    x = keras_tensor.keras_tensor_from_type_spec(spec, name=name)
else:
    with get_graph().as_default():
        if sparse:
            x = array_ops.sparse_placeholder(dtype, shape=shape, name=name)
        elif ragged:
            ragged_rank = 0
            for i in range(1, len(shape)):
                if shape[i] is None:
                    ragged_rank = i
            type_spec = ragged_tensor.RaggedTensorSpec(
                shape=shape, dtype=dtype, ragged_rank=ragged_rank)
            def tensor_spec_to_placeholder(tensorspec):
                exit(array_ops.placeholder(tensorspec.dtype, tensorspec.shape))
            x = nest.map_structure(tensor_spec_to_placeholder, type_spec,
                                   expand_composites=True)
        else:
            x = array_ops.placeholder(dtype, shape=shape, name=name)

if context.executing_eagerly():
    # Add keras_history connectivity information to the placeholder
    # when the placeholder is built in a top-level eager context
    # (intended to be used with keras.backend.function)
    from tensorflow.python.keras.engine import input_layer  # pylint: disable=g-import-not-at-top
    x = input_layer.Input(tensor=x)
    x._is_backend_placeholder = True

exit(x)
