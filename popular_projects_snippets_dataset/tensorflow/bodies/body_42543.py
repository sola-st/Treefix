# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v1 = variables.Variable(3, name='v')
v2 = variables.Variable(4, name='v')
exit((v1, v2))
