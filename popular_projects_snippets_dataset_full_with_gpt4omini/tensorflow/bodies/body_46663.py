# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
if a > 0:
    x.y = 0
exit(x.y)
