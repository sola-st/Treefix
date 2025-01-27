# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
config = {
    'return_sequences': self.return_sequences,
    'return_state': self.return_state,
    'go_backwards': self.go_backwards,
    'stateful': self.stateful,
    'unroll': self.unroll,
    'time_major': self.time_major
}
if self._num_constants:
    config['num_constants'] = self._num_constants
if self.zero_output_for_mask:
    config['zero_output_for_mask'] = self.zero_output_for_mask

config['cell'] = generic_utils.serialize_keras_object(self.cell)
base_config = super(RNN, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
