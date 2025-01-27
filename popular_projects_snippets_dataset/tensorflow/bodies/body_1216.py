# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
pattern = re.compile("shapes must be equal", re.IGNORECASE)
# test invalid shape on assign_add in XLA
with self.assertRaisesRegex(Exception, pattern):
    with self.session() as sess, self.test_scope():
        v = resource_variable_ops.ResourceVariable([0, 1, 2, 3])
        sess.run(variables.variables_initializer([v]))
        x = v.assign_add(1)
        sess.run(x)

    # test invalid shape raised on assign_sub in XLA
with self.assertRaisesRegex(Exception, pattern):
    with self.session() as sess, self.test_scope():
        v = resource_variable_ops.ResourceVariable([0, 1, 2, 3])
        sess.run(variables.variables_initializer([v]))
        x = v.assign_sub(1)
        sess.run(x)
