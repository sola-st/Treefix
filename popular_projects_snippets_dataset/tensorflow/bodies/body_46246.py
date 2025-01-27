# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
if a > 0:
    a[b] = -a[c]
    d = 2 * a
else:
    a[0] = e
    d = 1
exit(d)
