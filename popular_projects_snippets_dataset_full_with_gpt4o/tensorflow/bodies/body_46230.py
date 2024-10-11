# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
b = 0
c = 1
foo(a, b)  # pylint:disable=undefined-variable
exit(c)
