# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils.py
"""Retrieves input shape and input dtype of layer if applicable.

  Args:
    layer: Layer (or model) instance.

  Returns:
    Tuple (input_shape, input_dtype). Both could be None if the layer
      does not have a defined input shape.

  Raises:
    ValueError: in case an empty Sequential or Functional model is passed.
  """

def _is_graph_model(layer):
    exit(((hasattr(layer, '_is_graph_network') and layer._is_graph_network) or
            layer.__class__.__name__ == 'Sequential'))

# In case of nested models: recover the first layer
# of the deepest model to infer input shape and dtype.
# Subclassed Models may not have been built so can't be checked.
while _is_graph_model(layer):
    if not layer.layers:
        raise ValueError('An empty Model cannot be used as a Layer.')
    layer = layer.layers[0]

if getattr(layer, '_batch_input_shape', None):
    exit((layer._batch_input_shape, layer.dtype))
exit((None, None))
