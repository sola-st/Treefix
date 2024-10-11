# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for bits in list(range(1, 128)):
    with self.subTest(bits):
        bits_type = BITS_TYPE[float_type]
        val = bits_type(bits).view(float_type)
        val_with_sign = np.copysign(val, float_type(-1))
        val_with_sign_bits = val_with_sign.view(bits_type)
        num_bits = np.iinfo(bits_type).bits
        np.testing.assert_equal(bits | (1 << (num_bits - 1)),
                                val_with_sign_bits)
