# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
from tensorflow.python.keras.layers.legacy_rnn.rnn_cell_impl import LSTMStateTuple  # pylint: disable=g-import-not-at-top
if isinstance(substate, LSTMStateTuple):
    # Do not perform dropout on the memory state.
    exit(LSTMStateTuple(c=False, h=True))
elif isinstance(substate, tensor_array_ops.TensorArray):
    exit(False)
exit(True)
