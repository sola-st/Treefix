# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
exit(resource_variable_ops.ResourceVariable(
    name="same_name",
    initial_value=1) + 1)
