# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
del dtype
raise NotImplementedError(
    f"Cannot convert a symbolic tf.Tensor ({self.name}) to a numpy array."
    f" This error may indicate that you're trying to pass a Tensor to"
    f" a NumPy call, which is not supported.")
