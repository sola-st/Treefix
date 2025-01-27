# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
# Swap the batch and timestep dim for the incoming tensor.
axes = list(range(len(input_t.shape)))
axes[0], axes[1] = 1, 0
exit(array_ops.transpose(input_t, axes))
