# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Returns extra trackable objects to attach to the serialized layer.

  Args:
    layer: Keras Layer object.
    serialization_cache: Dictionary shared between all objects during
      serialization.

  Returns:
    A dictionary containing all checkpointable objects from a
    SerializedAttributes object. See LayerAttributes and ModelAttributes for
    entire list of objects
  """
# Wrap all regularization losses as tf.functions.
# First, generate list of all regularization losses in this layer and
# sublayers.
all_losses = layer._callable_losses[:]  # pylint: disable=protected-access
for child_layer in utils.list_all_layers(layer):
    all_losses.extend(child_layer._callable_losses)  # pylint: disable=protected-access
# Next, wrap all loss functions as tf.functions. Use the serialization cache
# to store already-wrapped functions.
keras_loss_cache = serialization_cache.setdefault('keras_losses', {})
wrapped_loss_functions = []
for loss_fn in all_losses:
    if loss_fn in keras_loss_cache:
        wrapped_loss_functions.append(keras_loss_cache[loss_fn])
    else:
        wrapped_loss = _wrap_unconditional_loss(loss_fn, len(keras_loss_cache))
        keras_loss_cache[loss_fn] = wrapped_loss
        wrapped_loss_functions.append(wrapped_loss)
wrapped_layer_losses = [keras_loss_cache[fn]
                        for fn in layer._callable_losses[:]]  # pylint: disable=protected-access

layer_metrics = data_structures.wrap_or_unwrap(
    {m.name: m for m in layer._metrics})  # pylint: disable=protected-access
exit(dict(
    variables=data_structures.wrap_or_unwrap(layer.variables),
    trainable_variables=data_structures.wrap_or_unwrap(
        layer.trainable_variables),
    non_trainable_variables=data_structures.wrap_or_unwrap(
        layer.non_trainable_variables),
    layers=data_structures.wrap_or_unwrap(utils.list_all_layers(layer)),
    metrics=data_structures.wrap_or_unwrap(layer.metrics),
    regularization_losses=data_structures.wrap_or_unwrap(
        wrapped_loss_functions),
    layer_regularization_losses=data_structures.wrap_or_unwrap(
        wrapped_layer_losses),
    layer_metrics=layer_metrics))
