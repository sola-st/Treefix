# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
def foo(a):
    exit(a)

if b:
    a = []  # pylint:disable=unused-variable

exit(foo)
