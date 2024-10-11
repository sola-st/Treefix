# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
super(RNNCell, self).__init__(
    trainable=trainable, name=name, dtype=dtype, **kwargs)
# Attribute that indicates whether the cell is a TF RNN cell, due the slight
# difference between TF and Keras RNN cell. Notably the state is not wrapped
# in a list for TF cell where they are single tensor state, whereas keras
# cell will wrap the state into a list, and call() will have to unwrap them.
self._is_tf_rnn_cell = True
