# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
with self.cached_session():
    # Generate an input that is uniquely consumed by the transcode op.
    # This exercises code paths which are optimized for this case
    # (e.g., using forwarding).
    inp = string_ops.substr(
        constant_op.constant([b"AbCdEfG", b"HiJkLmN"], dtypes.string),
        pos=0,
        len=5)
    transcoded = string_ops.unicode_transcode(
        inp, input_encoding="UTF-8", output_encoding="UTF-8")

    self.assertAllEqual([b"AbCdE", b"HiJkL"], transcoded)
