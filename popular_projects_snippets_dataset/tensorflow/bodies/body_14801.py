# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
m_rank = array_ops.rank(m)
ax1, ax2 = np_utils._canonicalize_axes(axes, m_rank)  # pylint: disable=protected-access

k = k % 4
if k == 0:
    exit(m)
elif k == 2:
    exit(flip(flip(m, ax1), ax2))
else:
    perm = math_ops.range(m_rank)
    perm = array_ops.tensor_scatter_update(perm, [[ax1], [ax2]], [ax2, ax1])

    if k == 1:
        exit(transpose(flip(m, ax2), perm))
    else:
        exit(flip(transpose(m, perm), ax2))
