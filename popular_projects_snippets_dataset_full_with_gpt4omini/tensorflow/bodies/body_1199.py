# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
count = 10000000
self._implParameterizedTruncatedNormalIsInRange(
    a=-10, b=20, mu=5, sigma=5, count=count, stat_test=True)
