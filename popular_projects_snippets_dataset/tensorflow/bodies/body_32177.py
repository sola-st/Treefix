# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/base64_ops_test.py
for pad in (False, True):
    for _ in range(10):
        msg = [np.random.bytes(np.random.randint(20))
               for _ in range(np.random.randint(10))]
        self._RunTest(msg, pad=pad)

    # Zero-element, non-trivial shapes.
    for _ in range(10):
        k = np.random.randint(10)
        msg = np.empty((0, k), dtype=bytes)
        encoded = string_ops.encode_base64(msg, pad=pad)
        decoded = string_ops.decode_base64(encoded)

        with self.cached_session() as sess:
            encoded_value, decoded_value = self.evaluate([encoded, decoded])

        self.assertEqual(encoded_value.shape, msg.shape)
        self.assertEqual(decoded_value.shape, msg.shape)
