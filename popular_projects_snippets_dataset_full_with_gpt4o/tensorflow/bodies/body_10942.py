# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
g = gradients_impl.gradients(y, x)
exit(g[0])
