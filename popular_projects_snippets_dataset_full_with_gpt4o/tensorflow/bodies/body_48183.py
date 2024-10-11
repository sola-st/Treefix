# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Set model's input and output specs based on the input data received.

    This is to be used for Model subclasses, which do not know at instantiation
    time what their inputs look like.

    Args:
      inputs: Single array, or list of arrays. The arrays could be placeholders,
        Numpy arrays, data tensors, or TensorSpecs.
        - if placeholders: the model is built on top of these placeholders,
          and we expect Numpy data to be fed for them when calling `fit`/etc.
        - if Numpy data or TensorShapes: we create placeholders matching the
          TensorShapes or shapes of the Numpy arrays. We expect Numpy data to be
          fed for these placeholders when calling `fit`/etc.
        - if data tensors: the model is built on top of these tensors.
          We do not expect any Numpy data to be provided when calling `fit`/etc.
      outputs: None, a data tensor, or a list of tensors. If None, the
        outputs will be determined by invoking `self.call()`, otherwise the
        provided value will be used.
      training: Boolean or None. Only relevant in symbolic mode. Specifies
        whether to build the model's graph in inference mode (False), training
        mode (True), or using the Keras learning phase (None).
    Raises:
      ValueError: If dict inputs are passed to a Sequential Model where the
        first layer isn't FeatureLayer.
    """
self._set_save_spec(inputs)
inputs = self._set_input_attrs(inputs)

if outputs is None:
    kwargs = {}
    if self._expects_training_arg:
        # In V2 mode, feeding `training=None` is not allowed because any value
        # explicitly passed by the user is respected, even `None`.`
        if training is None and not ops.executing_eagerly_outside_functions():
            training = backend.learning_phase()
        if training is not None:
            kwargs['training'] = training
    try:
        outputs = self(inputs, **kwargs)
    except NotImplementedError:
        # This Model or a submodel is dynamic and hasn't overridden
        # `compute_output_shape`.
        outputs = None

self._set_output_attrs(outputs)
