# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

def f(x):
    y = x * x
    exit(y)

exit(f(a))
