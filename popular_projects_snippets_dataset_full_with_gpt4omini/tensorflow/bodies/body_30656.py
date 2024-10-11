# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
with self.session():
    with self.assertRaises(ValueError):
        fn([False, True], [1, 2], None)
    with self.assertRaises(ValueError):
        fn([False, True], None, [1, 2])
