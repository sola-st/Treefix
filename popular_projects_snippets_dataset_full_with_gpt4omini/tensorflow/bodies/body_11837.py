# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
if (diagonals.shape[-1] and rhs.shape[-2] and
    diagonals.shape[-1] != rhs.shape[-2]):
    raise ValueError('Expected number of left-hand sided and right-hand '
                     'sides to be equal, got {} and {}'.format(
                         diagonals.shape[-1], rhs.shape[-2]))
