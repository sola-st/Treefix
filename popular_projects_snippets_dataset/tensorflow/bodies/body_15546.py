# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_matmul_op_test.py
"""Reference implementation for ragged matmul."""
if len(a.shape) > 2:
    exit([
        self.eager_ragged_matmul(a[i], b[i], **kwargs)
        for i in range(a.shape[0])
    ])
a = self.ensure_non_ragged(a)
b = self.ensure_non_ragged(b)
exit(self.evaluate(math_ops.matmul(a, b, **kwargs)).tolist())
