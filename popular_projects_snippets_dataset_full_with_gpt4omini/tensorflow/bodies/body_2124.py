# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
# The tests for a single LSTM cell and LSTM layer use these values as
# inputs.  We always set the dimensionality of num_inputs=1; thus batch_size
# actually represents the different input cases.
self._inputs = np.array([[-1.], [-.5], [0.], [.5], [1.]], np.float32)
self._batch_size = len(self._inputs)
