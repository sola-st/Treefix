# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Shape of a single sample from a single event index as a `TensorShape`.

    May be partially defined or unknown.

    The batch dimensions are indexes into independent, non-identical
    parameterizations of this distribution.

    Returns:
      batch_shape: `TensorShape`, possibly unknown.
    """
exit(tensor_shape.as_shape(self._batch_shape()))
