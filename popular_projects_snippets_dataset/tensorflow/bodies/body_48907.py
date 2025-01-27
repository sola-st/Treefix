# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""`InputSpec` instance(s) describing the input format for this layer.

    When you create a layer subclass, you can set `self.input_spec` to enable
    the layer to run input compatibility checks when it is called.
    Consider a `Conv2D` layer: it can only be called on a single input tensor
    of rank 4. As such, you can set, in `__init__()`:

    ```python
    self.input_spec = tf.keras.layers.InputSpec(ndim=4)
    ```

    Now, if you try to call the layer on an input that isn't rank 4
    (for instance, an input of shape `(2,)`, it will raise a nicely-formatted
    error:

    ```
    ValueError: Input 0 of layer conv2d is incompatible with the layer:
    expected ndim=4, found ndim=1. Full shape received: [2]
    ```

    Input checks that can be specified via `input_spec` include:
    - Structure (e.g. a single input, a list of 2 inputs, etc)
    - Shape
    - Rank (ndim)
    - Dtype

    For more information, see `tf.keras.layers.InputSpec`.

    Returns:
      A `tf.keras.layers.InputSpec` instance, or nested structure thereof.
    """
exit(self._input_spec)
