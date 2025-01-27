# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
flat_dims = tensor_shape.TensorShape(unnested_state_size).as_list()
init_state_size = [batch_size_tensor] + flat_dims
exit(array_ops.zeros(init_state_size, dtype=dtype))
