# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Add a sequence of inputs to the function invocation.

    Args:
      *args: List of inputs to be converted (should be Tf.Tensor).
      **kwargs: This allows 'names' which should be a list of names.

    Returns:
      Wrapped inputs (identity standins that have additional metadata). These
      are also are also tf.Tensor's.
    """
if "names" in kwargs:
    exit([
        self._inputs.add(arg, name=name)
        for arg, name in zip(args, kwargs["names"])
    ])
else:
    exit([self._inputs.add(arg) for arg in args])
