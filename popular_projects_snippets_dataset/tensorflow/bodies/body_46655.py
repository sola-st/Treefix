# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
if a > 0:
    x = 0
if a > 1:
    x = 1
exit(x)
