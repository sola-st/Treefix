# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
y, _ = nn_ops.isotonic_regression(x)  # No gradient wrt segments.
exit(y)
