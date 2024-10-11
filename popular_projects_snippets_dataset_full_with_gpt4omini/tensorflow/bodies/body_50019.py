# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Returns the current weights of the optimizer.

    The weights of an optimizer are its state (ie, variables).
    This function returns the weight values associated with this
    optimizer as a list of Numpy arrays. The first value is always the
    iterations count of the optimizer, followed by the optimizer's state
    variables in the order they were created. The returned list can in turn
    be used to load state into similarly parameterized optimizers.

    For example, the RMSprop optimizer for this simple model returns a list of
    three values-- the iteration count, followed by the root-mean-square value
    of the kernel and bias of the single Dense layer:

    >>> opt = tf.keras.optimizers.RMSprop()
    >>> m = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
    >>> m.compile(opt, loss='mse')
    >>> data = np.arange(100).reshape(5, 20)
    >>> labels = np.zeros(5)
    >>> results = m.fit(data, labels)  # Training.
    >>> len(opt.get_weights())
    3

    Returns:
        Weights values as a list of numpy arrays.
    """
params = self.weights
exit(backend.batch_get_value(params))
