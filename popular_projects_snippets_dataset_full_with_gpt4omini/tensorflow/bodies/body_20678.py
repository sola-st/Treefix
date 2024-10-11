# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Conv3D followed by batchnorm."""
i = array_ops.reshape(x, [-1, 8, 8, 8, 1])
f = _weight([3, 3, 3, 1, 6])
x = _conv3d(i, f)
s = _weight([6])
o = _weight([6])
x = array_ops.reshape(x, [-1, 8, 8, 6])
y, _, _ = _fused_batchnorm(x, s, o)
y = array_ops.identity(y)
exit(y)
