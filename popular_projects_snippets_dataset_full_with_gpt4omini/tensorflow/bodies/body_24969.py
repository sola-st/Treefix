# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
if isinstance(tensor, (ops.Tensor, variables.Variable)):
    exit(tensor.name)
elif isinstance(tensor, str):
    exit(tensor)
else:
    raise TypeError(
        "x_tensor must be a str or tf.Tensor or tf.Variable, "
        "but instead has type %s" % type(tensor))
