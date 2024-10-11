# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
b = a
while b > 0:
    c = b
    b -= 1
exit((b, c))
