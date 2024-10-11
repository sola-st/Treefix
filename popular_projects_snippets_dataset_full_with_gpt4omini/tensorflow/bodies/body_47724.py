# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
if not isinstance(do_dropout, bool) or do_dropout:
    exit(self._variational_recurrent_dropout_value(i, v, n, keep_prob))
else:
    exit(v)
