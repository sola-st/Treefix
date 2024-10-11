# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Matmul followed by activation."""
i = array_ops.reshape(x, [8, 8])
f = _weight([8, 8])
x = math_ops.matmul(i, f)
y = nn.relu(x)
exit(y)
