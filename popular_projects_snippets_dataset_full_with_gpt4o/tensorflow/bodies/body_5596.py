# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(1.)
with self.cached_session():
    self.evaluate(variables_lib.global_variables_initializer())
    self.assertEqual(v.eval(), 1.)
