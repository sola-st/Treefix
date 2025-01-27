# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
max(a)  # pylint:disable=used-before-assignment
a = 1
exit(a)
