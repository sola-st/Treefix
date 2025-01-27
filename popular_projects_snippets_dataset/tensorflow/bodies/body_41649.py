# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if not created_variables:
    created_variables.append(variables.Variable(1.))
exit(created_variables[0] + 1.)
