# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable([0, 1, 2, 3])
self.evaluate(v.initializer)
pattern = re.compile("shapes must be equal", re.IGNORECASE)
with self.assertRaisesRegex(Exception, pattern):
    self.evaluate(v.assign_add(1))
