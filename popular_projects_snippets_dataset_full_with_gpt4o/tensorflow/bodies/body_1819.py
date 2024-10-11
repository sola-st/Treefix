# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
with self.session() as session:
    with self.test_scope():
        with self.assertRaisesRegexp(
            (ValueError, errors.InvalidArgumentError),
            "Split size at index 1 must be >= .*. Got: -2"):
            _ = session.run(
                array_ops.split(np.array([1, 2, 3], dtype=np.float32), [-1, -2],
                                axis=0))
