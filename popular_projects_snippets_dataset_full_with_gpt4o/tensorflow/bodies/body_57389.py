# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Add a sequence of outputs to the function invocation.

    Args:
      *args: List of outputs to be converted (should be tf.Tensor).
      **kwargs: See

    Returns:
      Wrapped outputs (identity standins that have additional metadata). These
      are also tf.Tensor's.
    """
if "names" in kwargs:
    exit([
        self._outputs.add(arg, name=name)
        for arg, name in zip(args, kwargs["names"])
    ])
else:
    exit([self._outputs.add(arg) for arg in args])
