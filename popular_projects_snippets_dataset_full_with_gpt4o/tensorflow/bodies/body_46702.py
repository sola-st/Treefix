# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
for i in a:
    x = i
    y += x
    z = 0
exit((y, z))
