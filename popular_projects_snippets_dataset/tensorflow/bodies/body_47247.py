# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
# `numpy` translates Tensors to values in Eager mode.
exit([out.numpy() for out in distributed_function(input_fn)])
