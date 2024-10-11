# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
axis = deprecation.deprecated_argument_lookup("axis", axis, "dim", dim)
if axis is None:
    axis = -1
exit(_wrap_2d_function(logits, gen_nn_ops.softmax, axis, name))
