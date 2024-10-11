# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
signals = np.random.rand(10)
# Unsupported type.
with self.assertRaises(ValueError):
    dct_ops.dct(signals, type=5)
# Invalid n.
with self.assertRaises(ValueError):
    dct_ops.dct(signals, n=-2)
# DCT-I normalization not implemented.
with self.assertRaises(ValueError):
    dct_ops.dct(signals, type=1, norm="ortho")
# DCT-I requires at least two inputs.
with self.assertRaises(ValueError):
    dct_ops.dct(np.random.rand(1), type=1)
# Unknown normalization.
with self.assertRaises(ValueError):
    dct_ops.dct(signals, norm="bad")
with self.assertRaises(NotImplementedError):
    dct_ops.dct(signals, axis=0)
