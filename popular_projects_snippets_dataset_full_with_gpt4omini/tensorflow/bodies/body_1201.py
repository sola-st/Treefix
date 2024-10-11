# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
count = 10000000
# the region is on the right side of the parent normal distribution
self._implParameterizedTruncatedNormalIsInRange(
    a=4, b=10, mu=0, sigma=1, count=count, stat_test=False)
self._implParameterizedTruncatedNormalIsInRange(
    a=4, b=np.infty, mu=0, sigma=1, count=count, stat_test=False)
