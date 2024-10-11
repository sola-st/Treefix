# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_logging_level_test.py
with self.cached_session():
    tensor = math_ops.range(10)
    with self.captureWritesToStream(sys.stderr) as printed:
        print_op = logging_ops.print_v2(
            tensor, output_stream=tf_logging.info)
        self.evaluate(print_op)
    self.assertTrue("I" in printed.contents())
    expected = "[0 1 2 ... 7 8 9]"
    self.assertTrue(expected in printed.contents())
