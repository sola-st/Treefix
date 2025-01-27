# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Retrieves the weights of the model.

    Returns:
        A flat list of Numpy arrays.
    """
strategy = (self._distribution_strategy or
            self._compile_time_distribution_strategy)
if strategy:
    with strategy.scope():
        exit(base_layer.Layer.get_weights(self))
exit(base_layer.Layer.get_weights(self))
