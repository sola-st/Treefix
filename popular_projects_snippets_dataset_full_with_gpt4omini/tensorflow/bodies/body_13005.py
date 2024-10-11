# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
exit(tensor_array_ops.TensorArray(
    dtype=dtype,
    size=time_steps,
    element_shape=element_shape,
    tensor_array_name=base_name + name))
