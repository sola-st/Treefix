# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/cudnn_recurrent.py
config = {
    'return_sequences': self.return_sequences,
    'return_state': self.return_state,
    'go_backwards': self.go_backwards,
    'stateful': self.stateful,
    'time_major': self.time_major,
}
base_config = super(  # pylint: disable=bad-super-call
    RNN, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
