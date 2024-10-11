# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
if x > 0:
    x = -x
    y = 2 * x
    z = -y
else:
    x = 2 * x
    y = -x
    u = -y
exit((z, u))
