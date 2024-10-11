# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
"""Returns the current value of the weights of the optimizer.

    Returns:
        A list of numpy arrays.
    """
exit(backend.batch_get_value(self.weights))
