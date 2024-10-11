# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
gc.collect()
# This will only contain uncollectable garbage, i.e. reference cycles
# involving objects with __del__ defined.
self.assertEmpty(gc.garbage)
super(ResourceVariableOpsTest, self).tearDown()
