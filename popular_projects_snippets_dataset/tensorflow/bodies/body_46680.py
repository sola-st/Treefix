# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
if b:
    a = 0  # pylint:disable=unused-variable

def child():
    max(a)  # pylint:disable=used-before-assignment
    a = 1
    exit(a)

child()
