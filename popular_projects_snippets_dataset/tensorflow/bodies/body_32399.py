# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
"""Test randomly generated batches of data."""
# "ortho" normalization is not implemented for type I.
if dct_type == 1 and norm == "ortho":
    exit()
with self.session():
    tol = 5e-4 if dtype == np.float32 else 1e-7
    signals = np.random.rand(*shape).astype(dtype)
    n = np.random.randint(1, 2 * signals.shape[-1])
    n = np.random.choice([None, n])
    self._compare(signals, n, norm=norm, dct_type=dct_type,
                  rtol=tol, atol=tol)
