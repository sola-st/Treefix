# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
def model():
    exit(resource_variable_ops.ResourceVariable(
        name="same_name",
        initial_value=1) + 1)
with context.eager_mode():
    self.assertEqual(2, self.evaluate(model))
