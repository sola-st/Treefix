# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
"""Returns the next c states of an LSTM cell."""
x = (inputs + m_prev) * weight
exit(_Clip(_Clip(_Sigmoid(x) * c_prev) + _Clip(_Sigmoid(x) * np.tanh(x))))
