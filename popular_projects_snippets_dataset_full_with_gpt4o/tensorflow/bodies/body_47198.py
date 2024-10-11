# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/models.py
"""Clone a functional `Model` instance.

  Model cloning is similar to calling a model on new inputs,
  except that it creates new layers (and thus new weights) instead
  of sharing the weights of the existing layers.

  Input layers are always cloned.

  Args:
      model: Instance of `Model`.
      input_tensors: optional list of input tensors
          to build the model upon. If not provided,
          placeholders will be created.
      layer_fn: callable to be applied on non-input layers in the model. By
          default it clones the layer. Another example is to preserve the layer
          to share the weights. This is required when we create a per-replica
          copy of the model with distribution strategy; we want the weights to
          be shared but still feed inputs separately so we create new input
          layers.

  Returns:
      An instance of `Model` reproducing the behavior
      of the original model, on top of new inputs tensors,
      using newly instantiated weights.

  Raises:
      ValueError: in case of invalid `model` argument value or `layer_fn`
      argument value.
  """
if not isinstance(model, Model):
    raise ValueError('Expected `model` argument '
                     'to be a `Model` instance, got ', model)
if isinstance(model, Sequential):
    raise ValueError('Expected `model` argument '
                     'to be a functional `Model` instance, '
                     'got a `Sequential` instance instead:', model)
if not model._is_graph_network:
    raise ValueError('Expected `model` argument '
                     'to be a functional `Model` instance, '
                     'but got a subclass model instead.')

new_input_layers = {}  # Cache for created layers.
if input_tensors is not None:
    # Make sure that all input tensors come from a Keras layer.
    input_tensors = nest.flatten(input_tensors)
    for i, input_tensor in enumerate(input_tensors):
        original_input_layer = model._input_layers[i]

        # Cache input layer. Create a new layer if the tensor is originally not
        # from a Keras layer.
        if not backend.is_keras_tensor(input_tensor):
            name = original_input_layer.name
            input_tensor = Input(tensor=input_tensor,
                                 name='input_wrapper_for_' + name)
            newly_created_input_layer = input_tensor._keras_history.layer
            new_input_layers[original_input_layer] = newly_created_input_layer
        else:
            new_input_layers[original_input_layer] = original_input_layer

if not callable(layer_fn):
    raise ValueError('Expected `layer_fn` argument to be a callable.')

model_configs, created_layers = _clone_layers_and_model_config(
    model, new_input_layers, layer_fn)
# Reconstruct model from the config, using the cloned layers.
input_tensors, output_tensors, created_layers = (
    functional.reconstruct_from_config(model_configs,
                                       created_layers=created_layers))
metrics_names = model.metrics_names
model = Model(input_tensors, output_tensors, name=model.name)
# Layers not directly tied to outputs of the Model, such as loss layers
# created in `add_loss` and `add_metric`.
ancillary_layers = [
    layer for layer in created_layers.values() if layer not in model.layers
]
# TODO(b/162887610): This may need to adjust the inbound node index if the
# created layers had already been used to define other models.
if ancillary_layers:
    new_nodes = nest.flatten([
        layer.inbound_nodes[1:]
        if functional._should_skip_first_node(layer)
        else layer.inbound_nodes for layer in created_layers.values()
    ])
    _insert_ancillary_layers(model, ancillary_layers, metrics_names, new_nodes)
exit(model)
