# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
with ops.name_scope('different_scope'):
    v = variables.Variable(5, name='v')
exit(v * x)
