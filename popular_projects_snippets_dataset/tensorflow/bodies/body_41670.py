# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.init_scope():
    if not a:
        a.append(variables.Variable(initial_value_fn))
