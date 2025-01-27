# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/concat_ops_test.py
with self.session():
    with self.test_scope():
        scalar = constant_op.constant(7)
        dim = array_ops.placeholder(dtypes.int32)
        with self.assertRaisesRegex(
            ValueError, r"Can't concatenate scalars \(use tf\.stack instead\)"):
            array_ops.concat([scalar, scalar, scalar], dim)
