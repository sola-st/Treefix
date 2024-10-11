# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.cached_session():
    # Initialize variable with a value different from the initial value passed
    # in the constructor.
    v = resource_variable_ops.ResourceVariable(2.0)
    v.initializer.run(feed_dict={v.initial_value: 3.0})
    self.assertEqual(3.0, v.value().eval())
