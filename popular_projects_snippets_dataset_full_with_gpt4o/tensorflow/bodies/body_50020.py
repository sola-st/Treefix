# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Set the weights of the optimizer.

    The weights of an optimizer are its state (ie, variables).
    This function takes the weight values associated with this
    optimizer as a list of Numpy arrays. The first value is always the
    iterations count of the optimizer, followed by the optimizer's state
    variables in the order they are created. The passed values are used to set
    the new state of the optimizer.

    For example, the RMSprop optimizer for this simple model takes a list of
    three values-- the iteration count, followed by the root-mean-square value
    of the kernel and bias of the single Dense layer:

    >>> opt = tf.keras.optimizers.RMSprop()
    >>> m = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
    >>> m.compile(opt, loss='mse')
    >>> data = np.arange(100).reshape(5, 20)
    >>> labels = np.zeros(5)
    >>> results = m.fit(data, labels)  # Training.
    >>> new_weights = [np.array(10), np.ones([20, 10]), np.zeros([10])]
    >>> opt.set_weights(new_weights)
    >>> opt.iterations
    <tf.Variable 'RMSprop/iter:0' shape=() dtype=int64, numpy=10>

    Args:
        weights: weight values as a list of numpy arrays.
    """
params = self.weights
if len(params) != len(weights):
    raise ValueError(
        "You called `set_weights(weights)` on optimizer " + self._name +
        " with a  weight list of length " + str(len(weights)) +
        ", but the optimizer was expecting " + str(len(params)) +
        " weights. Provided weights: " + str(weights)[:50] + "...")
if not params:
    exit()
weight_value_tuples = []
param_values = backend.batch_get_value(params)
for pv, p, w in zip(param_values, params, weights):
    if pv.shape != w.shape:
        raise ValueError("Optimizer weight shape " + str(pv.shape) +
                         " not compatible with "
                         "provided weight shape " + str(w.shape))
    weight_value_tuples.append((p, w))
backend.batch_set_value(weight_value_tuples)
