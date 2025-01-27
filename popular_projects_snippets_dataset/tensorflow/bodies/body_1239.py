# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
with self.assertRaisesRegex(errors.FailedPreconditionError,
                            "uninitialized"):
    with self.session() as sess, self.test_scope():
        v = resource_variable_ops.ResourceVariable([1, 2])
        sess.run(v[:].assign([1, 2]))
