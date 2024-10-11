# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with session.Session():
    var = self.make_variable()
    slice_op = var[3::1, 3::1, 3::1]
    self.run_and_time(slice_op)
