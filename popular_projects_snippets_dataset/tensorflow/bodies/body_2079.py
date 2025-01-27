# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
with self.session() as session:
    with self.test_scope():
        output = xla.dynamic_slice(
            np.arange(1000, dtype=np.int32).reshape([10, 10, 10]),
            np.array([5, 7, 3]), np.array([2, 3]))
    with self.assertRaises(errors.InvalidArgumentError) as invalid_arg_error:
        session.run(output)
    self.assertRegex(
        invalid_arg_error.exception.message,
        (r'has mismatched number of slice sizes \(2\) and number of start'
         r' indices \(3\)'))
