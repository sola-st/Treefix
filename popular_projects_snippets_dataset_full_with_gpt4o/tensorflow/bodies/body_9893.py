# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_utils_test.py
v = variables.Variable(variable_value, name=variable_name)
sess.run(variables.global_variables_initializer())
self.assertEqual(variable_value, v.eval())
