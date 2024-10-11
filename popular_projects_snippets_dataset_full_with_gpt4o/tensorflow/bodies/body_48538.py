# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# It turns out to be more performant to make a new set of indices rather
# than reusing the same range Tensor. (presumably because of buffer
# forwarding.)
indices = math_ops.range(num_samples, dtype=dtypes.int64)
if shuffle and shuffle != "batch":
    indices = random_ops.random_shuffle(indices)
exit(indices)
