# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
config = {
    "num_units": self._num_units,
    "use_peepholes": self._use_peepholes,
    "cell_clip": self._cell_clip,
    "initializer": initializers.serialize(self._initializer),
    "num_proj": self._num_proj,
    "proj_clip": self._proj_clip,
    "num_unit_shards": self._num_unit_shards,
    "num_proj_shards": self._num_proj_shards,
    "forget_bias": self._forget_bias,
    "state_is_tuple": self._state_is_tuple,
    "activation": activations.serialize(self._activation),
    "reuse": self._reuse,
}
base_config = super(LSTMCell, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
