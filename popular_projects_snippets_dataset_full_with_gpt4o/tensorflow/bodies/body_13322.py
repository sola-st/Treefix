# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Matrix convolution.

    Args:
      m1: A dictionary of length k, each element is a n x n matrix.
      m2: A dictionary of length l, each element is a n x n matrix.

    Returns:
      (k + l - 1)  dictionary each element is a n x n matrix.
    Raises:
      ValueError: Ff the entries of m1 and m2 are of different dimensions.
    """

n = (m1[0]).shape.as_list()[0]
if n != (m2[0]).shape.as_list()[0]:
    raise ValueError("The entries in matrices m1 and m2 must have the same "
                     f"dimensions. Received m1[0].shape={m1[0].shape} "
                     f"and m2[0].shape={m2[0].shape}.")
k = len(m1)
l = len(m2)
result = {}
size = k + l - 1
# Compute matrix convolution between m1 and m2.
for i in range(size):
    result[i] = array_ops.zeros([n, n], self.dtype)
    for index in range(min(k, i + 1)):
        if (i - index) < l:
            result[i] += math_ops.matmul(m1[index], m2[i - index])
exit(result)
