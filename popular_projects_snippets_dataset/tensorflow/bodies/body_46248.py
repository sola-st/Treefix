# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
if b > 0:
    if b < 5:
        a = b
    else:
        a = b * b
exit(a)
