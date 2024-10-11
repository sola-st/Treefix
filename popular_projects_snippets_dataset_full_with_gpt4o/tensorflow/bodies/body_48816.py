# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Retrieves the weights of the model.

    Returns:
        A flat list of Numpy arrays.
    """
with self.distribute_strategy.scope():
    exit(super(Model, self).get_weights())
