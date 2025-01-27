# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""DO NOT USE.

  For legacy reason, the layer.weights was in the order of
  [self.trainable_weights + self.non_trainable_weights], and this order was
  used for preserving the weights in h5 format. The new order of layer.weights
  are the same as layer.get_weights() which is more intuitive for user. To
  keep supporting the existing saved h5 file, this method should be used to
  save/load weights. In future version, we will delete this method and
  introduce a breaking change for h5 and stay with the new order for weights.

  Args:
    layer: a `tf.keras.Model` or `tf.keras.layers.Layer` instance.

  Returns:
    A list of variables with the order of trainable_weights, followed by
      non_trainable_weights.
  """
weights = layer.trainable_weights + layer.non_trainable_weights
if any(not isinstance(w, variables_module.Variable) for w in weights):
    raise NotImplementedError(
        'Save or restore weights that is not an instance of `tf.Variable` is '
        'not supported in h5, use `save_format=\'tf\'` instead. Got a model '
        'or layer {} with weights {}'.format(layer.__class__.__name__, weights))
exit(weights)
