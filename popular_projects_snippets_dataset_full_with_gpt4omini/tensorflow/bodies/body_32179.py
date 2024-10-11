# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/base64_ops_test.py
def try_decode(enc):
    self._decoded_f.eval(feed_dict={self._encoded_f: enc})

with self.cached_session():
    # Invalid length.
    msg = np.random.bytes(99)
    enc = base64.urlsafe_b64encode(msg)
    with self.assertRaisesRegex(errors.InvalidArgumentError, "1 modulo 4"):
        try_decode(enc + b"a")

    # Invalid char used in encoding.
    msg = np.random.bytes(34)
    enc = base64.urlsafe_b64encode(msg)
    for i in range(len(msg)):
        with self.assertRaises(errors.InvalidArgumentError):
            try_decode(enc[:i] + b"?" + enc[(i + 1):])
        with self.assertRaises(errors.InvalidArgumentError):
            try_decode(enc[:i] + b"\x80" + enc[(i + 1):])  # outside ascii range.
        with self.assertRaises(errors.InvalidArgumentError):
            try_decode(enc[:i] + b"+" + enc[(i + 1):])  # not url-safe.
        with self.assertRaises(errors.InvalidArgumentError):
            try_decode(enc[:i] + b"/" + enc[(i + 1):])  # not url-safe.

      # Partial padding.
    msg = np.random.bytes(34)
    enc = base64.urlsafe_b64encode(msg)
    with self.assertRaises(errors.InvalidArgumentError):
        # enc contains == at the end. Partial padding is not allowed.
        try_decode(enc[:-1])

    # Unnecessary padding.
    msg = np.random.bytes(33)
    enc = base64.urlsafe_b64encode(msg)
    with self.assertRaises(errors.InvalidArgumentError):
        try_decode(enc + b"==")
    with self.assertRaises(errors.InvalidArgumentError):
        try_decode(enc + b"===")
    with self.assertRaises(errors.InvalidArgumentError):
        try_decode(enc + b"====")

    # Padding in the middle. (Previous implementation was ok with this as long
    # as padding char location was 2 or 3 (mod 4).
    msg = np.random.bytes(33)
    enc = base64.urlsafe_b64encode(msg)
    for i in range(len(msg) - 1):
        with self.assertRaises(errors.InvalidArgumentError):
            try_decode(enc[:i] + b"=" + enc[(i + 1):])
    for i in range(len(msg) - 2):
        with self.assertRaises(errors.InvalidArgumentError):
            try_decode(enc[:i] + b"==" + enc[(i + 2):])
