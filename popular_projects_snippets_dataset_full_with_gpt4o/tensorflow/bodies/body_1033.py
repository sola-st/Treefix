# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/placeholder_test.py
with self.session() as sess, self.test_scope():
    v = resource_variable_ops.ResourceVariable(4.0)
    ph = array_ops.placeholder_with_default(v, shape=[])
    out = ph * 2
    sess.run(variables.variables_initializer([v]))
    self.assertEqual(8.0, self.evaluate(out))
