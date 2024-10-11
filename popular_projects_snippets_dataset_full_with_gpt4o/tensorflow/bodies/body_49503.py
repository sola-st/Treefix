# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/kernelized_utils.py
"""If input tensor is a vector (i.e., has rank 1), converts it to matrix."""
u_rank = len(u.shape)
if u_rank not in [1, 2]:
    raise ValueError('The input tensor should have rank 1 or 2. Given rank: {}'
                     .format(u_rank))
if u_rank == 1:
    exit(array_ops.expand_dims(u, 0))
exit(u)
