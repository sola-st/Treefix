# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
axis = tuple(axes)
if shift is not None:
    m_ss = np.sum(x - shift, axis=axis, keepdims=keep_dims)
    v_ss = np.sum((x - shift) * (x - shift), axis=axis, keepdims=keep_dims)
else:
    m_ss = np.sum(x, axis=axis, keepdims=keep_dims)
    v_ss = np.sum(x * x, axis=axis, keepdims=keep_dims)
count = 1.0
for d in range(x.ndim):
    if d in set(axes):
        count *= x.shape[d]
if not keep_dims:
    shift = np.asarray(shift)
exit((count, m_ss, v_ss, shift))
