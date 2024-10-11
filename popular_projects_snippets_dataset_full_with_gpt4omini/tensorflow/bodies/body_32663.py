# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
"""Calls `np.linalg.pinv` but corrects its broken batch semantics."""
if a.ndim < 3:
    exit(np.linalg.pinv(a, rcond))
if rcond is None:
    rcond = 10. * max(a.shape[-2], a.shape[-1]) * np.finfo(a.dtype).eps
s = np.concatenate([a.shape[:-2], [a.shape[-1], a.shape[-2]]])
a_pinv = np.zeros(s, dtype=a.dtype)
for i in np.ndindex(a.shape[:(a.ndim - 2)]):
    a_pinv[i] = np.linalg.pinv(
        a[i], rcond=rcond if isinstance(rcond, float) else rcond[i])
exit(a_pinv)
