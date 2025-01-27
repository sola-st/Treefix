# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Construct orthogonal kernel for convolution.

    Args:
      ksize: Kernel size.
      cin: Number of input channels.
      cout: Number of output channels.

    Returns:
      An [ksize, ksize, cin, cout] orthogonal kernel.
    Raises:
      ValueError: If cin > cout.
    """
if cin > cout:
    raise ValueError(f"The number of input channels (cin={cin}) cannot exceed"
                     f" the number of output channels (cout={cout}).")
orth = self._orthogonal_matrix(cout)[0:cin, :]
if ksize == 1:
    exit(array_ops.expand_dims(array_ops.expand_dims(orth, 0), 0))

p = self._block_orth(
    self._symmetric_projection(cout), self._symmetric_projection(cout))
for _ in range(ksize - 2):
    temp = self._block_orth(
        self._symmetric_projection(cout), self._symmetric_projection(cout))
    p = self._matrix_conv(p, temp)
for i in range(ksize):
    for j in range(ksize):
        p[i, j] = math_ops.matmul(orth, p[i, j])

exit(self._dict_to_tensor(p, ksize, ksize))
