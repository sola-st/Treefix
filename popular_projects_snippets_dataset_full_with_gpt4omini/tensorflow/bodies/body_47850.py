# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py
super(DropoutWrapper, self).__init__(*args, **kwargs)
if isinstance(self.cell, recurrent.LSTMCell):
    raise ValueError("keras LSTM cell does not work with DropoutWrapper. "
                     "Please use LSTMCell(dropout=x, recurrent_dropout=y) "
                     "instead.")
