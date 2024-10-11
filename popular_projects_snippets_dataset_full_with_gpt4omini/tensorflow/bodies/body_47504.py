# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Check whether the state_size contains multiple states."""
exit((hasattr(state_size, '__len__') and
        not isinstance(state_size, tensor_shape.TensorShape)))
