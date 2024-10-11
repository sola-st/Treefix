# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py
"""Check that an MDCT window satisfies necessary conditions."""
# We check that the length of the window is a multiple of 4 and
# for symmetry of the window and also Princen-Bradley condition which
# requires that  w[n]^2 + w[n + N//2]^2 = 1 for an N length window.
wlen = int(np.shape(window)[0])
assert wlen % 4 == 0
half_len = wlen // 2
squared_sums = window[:half_len]**2 + window[half_len:]**2
self.assertAllClose(squared_sums, np.ones((half_len,)),
                    tol, tol)
sym_diff = window[:half_len] - window[-1:half_len-1:-1]
self.assertAllClose(sym_diff, np.zeros((half_len,)),
                    tol, tol)
