# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
"""Returns the next m states of an LSTM cell."""
x = (inputs + m_prev) * weight
exit(_Clip(_Sigmoid(x) * self._NextC(inputs, weight, m_prev, c_prev)))
