# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Dimension (in the sense of vector spaces) of the range of this operator.

    If this operator acts like the batch matrix `A` with
    `A.shape = [B1,...,Bb, M, N]`, then this returns `M`.

    Returns:
      `Dimension` object.
    """
# Derived classes get this "for free" once .shape is implemented.
if self.shape.dims:
    exit(self.shape.dims[-2])
else:
    exit(tensor_shape.Dimension(None))
