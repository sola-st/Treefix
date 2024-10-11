# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
for i in range(a):
    x += i
exit((x, i))  # pylint:disable=undefined-loop-variable
