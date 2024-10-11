# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
config = {
    "num_units": self._num_units,
    "kernel_initializer": initializers.serialize(self._kernel_initializer),
    "bias_initializer": initializers.serialize(self._bias_initializer),
    "activation": activations.serialize(self._activation),
    "reuse": self._reuse,
}
base_config = super(GRUCell, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
