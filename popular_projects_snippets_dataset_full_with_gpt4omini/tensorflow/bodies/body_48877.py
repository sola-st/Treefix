# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Creates the variables of the layer (optional, for subclass implementers).

    This is a method that implementers of subclasses of `Layer` or `Model`
    can override if they need a state-creation step in-between
    layer instantiation and layer call.

    This is typically used to create the weights of `Layer` subclasses.

    Args:
      input_shape: Instance of `TensorShape`, or list of instances of
        `TensorShape` if the layer expects a list of inputs
        (one instance per input).
    """
# Only record the build input shapes of overridden build methods.
if not hasattr(self.build, '_is_default'):
    self._build_input_shape = input_shape
self.built = True
