# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""This is where the layer's logic lives.

    Note here that `call()` method in `tf.keras` is little bit different
    from `keras` API. In `keras` API, you can pass support masking for
    layers as additional arguments. Whereas `tf.keras` has `compute_mask()`
    method to support masking.

    Args:
      inputs: Input tensor, or dict/list/tuple of input tensors.
        The first positional `inputs` argument is subject to special rules:
        - `inputs` must be explicitly passed. A layer cannot have zero
          arguments, and `inputs` cannot be provided via the default value
          of a keyword argument.
        - NumPy array or Python scalar values in `inputs` get cast as tensors.
        - Keras mask metadata is only collected from `inputs`.
        - Layers are built (`build(input_shape)` method)
          using shape info from `inputs` only.
        - `input_spec` compatibility is only checked against `inputs`.
        - Mixed precision input casting is only applied to `inputs`.
          If a layer has tensor arguments in `*args` or `**kwargs`, their
          casting behavior in mixed precision should be handled manually.
        - The SavedModel input specification is generated using `inputs` only.
        - Integration with various ecosystem packages like TFMOT, TFLite,
          TF.js, etc is only supported for `inputs` and not for tensors in
          positional and keyword arguments.
      *args: Additional positional arguments. May contain tensors, although
        this is not recommended, for the reasons above.
      **kwargs: Additional keyword arguments. May contain tensors, although
        this is not recommended, for the reasons above.
        The following optional keyword arguments are reserved:
        - `training`: Boolean scalar tensor of Python boolean indicating
          whether the `call` is meant for training or inference.
        - `mask`: Boolean input mask. If the layer's `call()` method takes a
          `mask` argument, its default value will be set to the mask generated
          for `inputs` by the previous layer (if `input` did come from a layer
          that generated a corresponding mask, i.e. if it came from a Keras
          layer with masking support).

    Returns:
      A tensor or list/tuple of tensors.
    """
exit(inputs)
