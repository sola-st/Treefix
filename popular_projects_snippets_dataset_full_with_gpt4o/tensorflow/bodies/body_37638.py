# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
with context.eager_mode():

    @def_function.function
    def prints():
        logging_ops.print_v2("A")
        logging_ops.print_v2("B")
        logging_ops.print_v2("C")

    with self.captureWritesToStream(sys.stderr) as printed:
        prints()
    self.assertTrue(("A\nB\nC\n"), printed.contents())
