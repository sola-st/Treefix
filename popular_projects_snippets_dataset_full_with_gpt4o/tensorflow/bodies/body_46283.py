# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
a = lambda a, b: d(lambda b=f: a + b + c)  # pylint: disable=undefined-variable
