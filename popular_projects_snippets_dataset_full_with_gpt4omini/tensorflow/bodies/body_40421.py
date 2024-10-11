# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
a = math_ops.add(x.value(), 1.0)
# Make sure convert_to_tensor works correctly with list of TensorNodes.
b = array_ops.stack([a, a], axis=0)
exit(math_ops.reduce_mean(b))
