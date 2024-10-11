# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
if a > 1:
    x = b
else:
    x = c
if d > 0:
    x = 0
exit(x)
