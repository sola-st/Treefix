# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Calls the model on new inputs.

    In this case `call` just reapplies
    all ops in the graph to the new inputs
    (e.g. build a new computational graph from the provided inputs).

    Note: This method should not be called directly. It is only meant to be
    overridden when subclassing `tf.keras.Model`.
    To call a model on an input, always use the `__call__` method,
    i.e. `model(inputs)`, which relies on the underlying `call` method.

    Args:
        inputs: Input tensor, or dict/list/tuple of input tensors.
        training: Boolean or boolean scalar tensor, indicating whether to run
          the `Network` in training mode or inference mode.
        mask: A mask or list of masks. A mask can be
            either a tensor or None (no mask).

    Returns:
        A tensor if there is a single output, or
        a list of tensors if there are more than one outputs.
    """
raise NotImplementedError('When subclassing the `Model` class, you should '
                          'implement a `call` method.')
