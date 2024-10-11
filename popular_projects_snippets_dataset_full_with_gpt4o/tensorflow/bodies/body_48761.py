# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
self._num_tensors = 2
self._getter = getter_lambda
self._distribute_strategy = distribution_strategy_context.get_strategy()

def raise_error(_):
    raise RuntimeError('This layer contains a static lookup table, which '
                       'cannot be changed via set_weights().')

self._setter = raise_error
