# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_replace_op_test.py
with self.cached_session():
    # Generate an input that is uniquely consumed by the regex op.
    # This exercises code paths which are optimized for this case
    # (e.g., using forwarding).
    inp = string_ops.substr(
        constant_op.constant(["AbCdEfG",
                              "HiJkLmN"], dtypes.string),
        pos=0,
        len=5)
    stripped = op(inp, "\\p{Ll}", ".")
    self.assertAllEqual([b"A.C.E", b"H.J.L"], stripped)
