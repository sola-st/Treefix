# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v = variables.Variable(6, name='v')
exit(v.assign_add(x))
