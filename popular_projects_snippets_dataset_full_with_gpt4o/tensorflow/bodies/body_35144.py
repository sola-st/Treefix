# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
# Uses the Kolmogorov-Smirnov test for goodness of fit.
if not stats:
    exit(True)  # If we can't test, return that the test passes.
ks, _ = stats.kstest(samples, stats.gamma(alpha, scale=1 / beta).cdf)
# Return True when the test passes.
exit(ks < 0.02)
