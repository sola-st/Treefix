# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/simple_save_test.py
v = variables.Variable(variable_value, name=variable_name)
self.evaluate(variables.global_variables_initializer())
self.assertEqual(variable_value, self.evaluate(v))
exit(v)
