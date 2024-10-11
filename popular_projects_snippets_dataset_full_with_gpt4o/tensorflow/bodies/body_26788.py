# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
# Test function that uses control flow. The True branch is never taken
concat = string_ops.string_join([filename, "abc"])
exit(control_flow_ops.cond(
    math_ops.equal(filename, "abc"),
    lambda: reader_ops.TextLineDataset(concat),
    lambda: reader_ops.TextLineDataset(filename)))
