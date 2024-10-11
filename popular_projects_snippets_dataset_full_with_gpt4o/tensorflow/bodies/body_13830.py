# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_test_util.py
if not np.isfinite(array).all():
    raise AssertionError("array was not all finite. %s" % array[:15])
