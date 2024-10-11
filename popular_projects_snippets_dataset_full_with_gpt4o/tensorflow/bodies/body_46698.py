# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
if a > 0:
    x = b
if c > 1:
    x = 0
exit(x)
