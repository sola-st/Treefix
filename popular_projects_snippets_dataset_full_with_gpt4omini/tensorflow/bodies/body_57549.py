# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Constructor for TFLiteConverter.

    Args:
      serving_funcs: A list functions of the serving func of the jax module, the
        model params should already be inlined. (e.g., `serving_func =
        functools.partial(model, params=params)`)
      inputs: Array of input tensor placeholders tuple,s like `jnp.zeros`. For
        example, wrapped in an array like
        "[('input1', input1), ('input2', input2)]]".
    Jax function is polymorphic, for example:
    ```python
    def add(a, b):
      return a + b
    ```
    Will yield different computations if different input signatures are passed
    in: Pass `add(10.0, 20.0)` will yield a scalar `add` while pass
      `add(np.random((100, 1)), np.random(100, 100))` will yield a broadcasting
      add.  We will need the input information to do tracing for the converter
      to properly convert the model. So it's important to pass in the desired
      `input placeholders` with the correct input shape/type.

    In the converted tflite model:
    Currently: the function name will be default to main, the output names will
    be the traced outputs. The output ordering shall match the serving function.
    """
super(TFLiteJaxConverterV2, self).__init__()
self._serving_funcs = serving_funcs
self._inputs = inputs
