# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/models.py
"""Substitute for model cloning that works for subclassed models.

  Subclassed models cannot be cloned because their topology is not serializable.
  To "instantiate" an identical model in a new TF graph, we reuse the original
  model object, but we clear its state.

  After calling this function on a model instance, you can use the model
  instance as if it were a model clone (in particular you can use it in a new
  graph).

  This method clears the state of the input model. It is thus destructive.
  However the original state can be restored fully by calling
  `_in_place_subclassed_model_state_restoration`.

  Args:
    model: Instance of a Keras model created via subclassing.

  Raises:
    ValueError: In case the model uses a subclassed model as inner layer.
  """
assert not model._is_graph_network  # Only makes sense for subclassed networks
# Select correct base class for new Model.
version_utils.swap_class(model.__class__, training.Model, training_v1.Model,
                         ops.executing_eagerly_outside_functions())
# Retrieve all layers tracked by the model as well as their attribute names
attributes_cache = {}
for name in dir(model):
    # Skip attrs that track other trackables.
    if name == 'submodules' or name == '_self_tracked_trackables':
        continue

    try:
        value = getattr(model, name)
    except (AttributeError, ValueError, TypeError):
        continue
    if isinstance(value, Layer):
        attributes_cache[name] = value
        assert value in model.layers
        if hasattr(value, 'layers') and value.layers:
            raise ValueError('We do not support the use of nested layers '
                             'in `model_to_estimator` at this time. Found nested '
                             'layer: %s' % value)
    elif isinstance(
        value, (list, tuple)) and name not in ('layers', '_layers', 'metrics',
                                               '_compile_metric_functions',
                                               '_output_loss_metrics'):
        # Handle case: list/tuple of layers (also tracked by the Network API).
        if value and all(isinstance(val, Layer) for val in value):
            raise ValueError('We do not support the use of list-of-layers '
                             'attributes in subclassed models used with '
                             '`model_to_estimator` at this time. Found list '
                             'model: %s' % name)

  # Replace layers on the model with fresh layers
layers_to_names = {value: key for key, value in attributes_cache.items()}
original_layers = list(
    model._flatten_layers(include_self=False, recursive=False))
setattr_tracking = model._setattr_tracking
model._setattr_tracking = False
model._self_tracked_trackables = []
for layer in original_layers:  # We preserve layer order.
    config = layer.get_config()
    # This will not work for nested subclassed models used as layers.
    # This would be theoretically possible to support, but would add complexity.
    # Only do it if users complain.
    if isinstance(layer, training.Model) and not layer._is_graph_network:
        raise ValueError('We do not support the use of nested subclassed models '
                         'in `model_to_estimator` at this time. Found nested '
                         'model: %s' % layer)
    fresh_layer = layer.__class__.from_config(config)
    name = layers_to_names[layer]
    setattr(model, name, fresh_layer)
    model._self_tracked_trackables.append(fresh_layer)

# Cache original model build attributes (in addition to layers)
if (not hasattr(model, '_original_attributes_cache') or
    model._original_attributes_cache is None):
    if model.built:
        attributes_to_cache = [
            'inputs',
            'outputs',
            'total_loss',
            'optimizer',
            'train_function',
            'test_function',
            'predict_function',
            '_training_endpoints',
            '_collected_trainable_weights',
            '_feed_inputs',
            '_feed_input_names',
            '_feed_input_shapes',
        ]
        for name in attributes_to_cache:
            attributes_cache[name] = getattr(model, name)
model._original_attributes_cache = attributes_cache
_reset_build_compile_trackers(model)
model._setattr_tracking = setattr_tracking
