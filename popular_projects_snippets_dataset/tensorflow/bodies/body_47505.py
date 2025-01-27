# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if inputs is not None:
    batch_size = array_ops.shape(inputs)[0]
    dtype = inputs.dtype
exit(_generate_zero_filled_state(batch_size, cell.state_size, dtype))
