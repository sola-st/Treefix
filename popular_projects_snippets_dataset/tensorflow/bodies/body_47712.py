# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
tensor_value = ops.convert_to_tensor_v2_with_dispatch(v)
const_value = tensor_util.constant_value(tensor_value)
exit((tensor_value, const_value))
