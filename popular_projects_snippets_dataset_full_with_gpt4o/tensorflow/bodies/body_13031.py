# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
lpl = np.exp(x) - z * x
if compute_full_loss:
    stirling_approx = z * np.log(z) - z + 0.5 * np.log(2. * np.pi * z)
    lpl += np.ma.masked_array(stirling_approx, mask=(z <= 1)).filled(0.)
exit(lpl)
