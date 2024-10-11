# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Normalized the input data."""
output = []
for inp in inputs:
    with ops.colocate_with(inp, ignore_existing=True):
        output.append(nn_impl.l2_normalize(inp, dim=1))
exit(output)
