# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
v = variables.VariableV1(variable_value, name=variable_name)
self.evaluate(variables.global_variables_initializer())
self.assertEqual(variable_value, self.evaluate(v))
