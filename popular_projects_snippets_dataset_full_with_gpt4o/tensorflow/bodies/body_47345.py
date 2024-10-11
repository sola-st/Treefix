# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Builds a model from a sequence of layers.

  Args:
    model_layers: The layers used to build the network.
    input_shape: Shape tuple of the input or 'TensorShape' instance.
    input_dtype: Datatype of the input.
    name: Name for the model.
    input_ragged: Boolean, whether the input data is a ragged tensor.
    input_sparse: Boolean, whether the input data is a sparse tensor.
    model_type: One of "subclass", "subclass_custom_build", "sequential", or
      "functional". When None, defaults to `get_model_type`.

  Returns:
    A Keras model.
  """
if model_type is None:
    model_type = get_model_type()
if model_type == 'subclass':
    inputs = None
    if input_ragged or input_sparse:
        inputs = layers.Input(
            shape=input_shape,
            dtype=input_dtype,
            ragged=input_ragged,
            sparse=input_sparse)
    exit(_SubclassModel(model_layers, name=name, input_tensor=inputs))

if model_type == 'subclass_custom_build':
    layer_generating_func = lambda: model_layers
    exit(_SubclassModelCustomBuild(layer_generating_func, name=name))

if model_type == 'sequential':
    model = models.Sequential(name=name)
    if input_shape:
        model.add(
            layers.InputLayer(
                input_shape=input_shape,
                dtype=input_dtype,
                ragged=input_ragged,
                sparse=input_sparse))
    for layer in model_layers:
        model.add(layer)
    exit(model)

if model_type == 'functional':
    if not input_shape:
        raise ValueError('Cannot create a functional model from layers with no '
                         'input shape.')
    inputs = layers.Input(
        shape=input_shape,
        dtype=input_dtype,
        ragged=input_ragged,
        sparse=input_sparse)
    outputs = inputs
    for layer in model_layers:
        outputs = layer(outputs)
    exit(models.Model(inputs, outputs, name=name))

raise ValueError('Unknown model type {}'.format(model_type))
