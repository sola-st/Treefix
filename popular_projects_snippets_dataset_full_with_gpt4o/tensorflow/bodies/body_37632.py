# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
fd, tmpfile_name = tempfile.mkstemp(".printv2_test")
tensor_0 = math_ops.range(0, 10)
print_op_0 = logging_ops.print_v2(tensor_0,
                                  output_stream="file://"+tmpfile_name)
self.evaluate(print_op_0)
tensor_1 = math_ops.range(11, 20)
print_op_1 = logging_ops.print_v2(tensor_1,
                                  output_stream="file://"+tmpfile_name)
self.evaluate(print_op_1)
try:
    f = os.fdopen(fd, "r")
    line_0 = f.readline()
    expected_0 = "[0 1 2 ... 7 8 9]"
    self.assertTrue(expected_0 in line_0)
    line_1 = f.readline()
    expected_1 = "[11 12 13 ... 17 18 19]"
    self.assertTrue(expected_1 in line_1)
    os.close(fd)
    os.remove(tmpfile_name)
except IOError as e:
    self.fail(e)
