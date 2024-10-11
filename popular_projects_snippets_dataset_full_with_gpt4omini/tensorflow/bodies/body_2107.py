# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm.py
"""Returns the shape of the weights for a single LSTM cell."""
# Dimension 0 accounts for combining x with the previous m state.
# Dimension 1 accounts for the in value and the (in, forget, out) gates.
exit([num_inputs + num_nodes, 4 * num_nodes])
