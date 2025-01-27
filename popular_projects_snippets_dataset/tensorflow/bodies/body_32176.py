# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/base64_ops_test.py
for pad in (False, True):
    self._RunTest(b"", pad=pad)

    for _ in range(100):
        length = np.random.randint(1024 * 1024)
        msg = np.random.bytes(length)
        self._RunTest(msg, pad=pad)
