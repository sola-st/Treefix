# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
config = {"device": self._device}
base_config = super(DeviceWrapperBase, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
