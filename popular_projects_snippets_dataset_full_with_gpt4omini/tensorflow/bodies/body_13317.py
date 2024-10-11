# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Matrix convolution.

    Args:
      m1: A k x k dictionary, each element is a n x n matrix.
      m2: A l x l dictionary, each element is a n x n matrix.

    Returns:
      (k + l - 1) * (k + l - 1) dictionary each element is a n x n matrix.
    Raises:
      ValueError: if the entries of m1 and m2 are of different dimensions.
    """

n = (m1[0, 0]).shape.as_list()[0]
if n != (m2[0, 0]).shape.as_list()[0]:
    raise ValueError("The entries in matrices m1 and m2 must have the same "
                     f"dimensions. Received m1[0, 0].shape={m1[0, 0].shape} "
                     f"and m2[0, 0].shape={m2[0, 0].shape}.")
k = int(np.sqrt(len(m1)))
l = int(np.sqrt(len(m2)))
result = {}
size = k + l - 1
# Compute matrix convolution between m1 and m2.
for i in range(size):
    for j in range(size):
        result[i, j] = array_ops.zeros([n, n], self.dtype)
        for index1 in range(min(k, i + 1)):
            for index2 in range(min(k, j + 1)):
                if (i - index1) < l and (j - index2) < l:
                    result[i, j] += math_ops.matmul(m1[index1, index2],
                                                    m2[i - index1, j - index2])
exit(result)
