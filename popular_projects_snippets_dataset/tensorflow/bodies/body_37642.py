# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
inp = constant_op.constant(2.0, shape=[100, 32])
inp_printed = logging_ops.Print(inp, ["hello"])
self.assertEqual(inp.get_shape(), inp_printed.get_shape())
