# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
config = {
    "num_units": self._num_units,
    "forget_bias": self._forget_bias,
    "state_is_tuple": self._state_is_tuple,
    "activation": activations.serialize(self._activation),
    "reuse": self._reuse,
}
base_config = super(BasicLSTMCell, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
