# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
"""Sets the weights of the optimizer, from Numpy arrays.

    Should only be called after computing the gradients
    (otherwise the optimizer has no weights).

    Args:
        weights: a list of Numpy arrays. The number of arrays and their shape
          must match number of the dimensions of the weights of the optimizer
          (i.e. it should match the output of `get_weights`).

    Raises:
        ValueError: in case of incompatible weight shapes.
    """
params = self.weights
if len(params) != len(weights):
    raise ValueError('Length of the specified weight list (' +
                     str(len(weights)) +
                     ') does not match the number of weights '
                     'of the optimizer (' + str(len(params)) + ')')
weight_value_tuples = []
param_values = backend.batch_get_value(params)
for pv, p, w in zip(param_values, params, weights):
    if pv.shape != w.shape:
        raise ValueError('Optimizer weight shape ' + str(pv.shape) +
                         ' not compatible with '
                         'provided weight shape ' + str(w.shape))
    weight_value_tuples.append((p, w))
backend.batch_set_value(weight_value_tuples)
