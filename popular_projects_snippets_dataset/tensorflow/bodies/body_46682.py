# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
for _ in a:
    if x:
        del y
    else:
        y = 0
