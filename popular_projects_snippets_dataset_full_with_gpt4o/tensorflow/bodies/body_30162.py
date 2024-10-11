# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with session.Session():
    var = self.make_variable()
    helper = BenchmarkSlice(var)
    slice_op = helper[::2, ::1, ::2]
    self.run_and_time(slice_op)
