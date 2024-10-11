# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tf_function_test.py
super().setUp()
# Clear the state for every test.
def_function.run_functions_eagerly(False)
