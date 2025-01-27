# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
c = a + b
# These two AddV2 cannot use the same argument in tf.function since an
# optimization pass will remove duplicate ops and only run it once.
d = a + c
exit((c, d))
