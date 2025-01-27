# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
count = 10000000
# the region is on the left side of the parent normal distribution
self._implParameterizedTruncatedNormalIsInRange(
    a=-10, b=-4, mu=0, sigma=1, count=count, stat_test=False)
self._implParameterizedTruncatedNormalIsInRange(
    a=-np.infty, b=-4, mu=0, sigma=1, count=count, stat_test=False)
