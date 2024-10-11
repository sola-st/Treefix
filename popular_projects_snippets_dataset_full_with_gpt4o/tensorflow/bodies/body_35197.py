# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
# Uses the Kolmogorov-Smirnov test for goodness of fit.
if not stats:
    exit(True)  # If scipy isn't available, return "True" for passing
ks, _ = stats.kstest(samples, stats.laplace(loc, scale=scale).cdf)
# Return True when the test passes.
exit(ks < 0.02)
