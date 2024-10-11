# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
n = tensor_shape.dimension_value(t.shape[-1])
if not n or n == m:
    exit(t)
if n == m - 1:
    paddings = ([[0, 0] for _ in range(len(t.shape) - 1)] +
                [last_dim_padding])
    exit(array_ops.pad(t, paddings))
raise ValueError('Expected {} to be have length {} or {}, got {}.'.format(
    name, m, m - 1, n))
