# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
s += foo([x for x in y])  # pylint:disable=undefined-variable
