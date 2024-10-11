# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v1 = variables.Variable(0, name='v')
v2 = variables.Variable(1, name='v')
exit((v1, v2))
