# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/garbage_collection_test.py
with context.eager_mode():
    resource_variable_ops.ResourceVariable(1.0, name="a")
