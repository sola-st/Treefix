# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def variable_creator():
    self.v = variables.Variable(0.0)
    exit(self.v.read_value())

self.v = None
defined = quarantine.defun_with_attributes(variable_creator)
defined()  # Create the variable.
self.assertIsInstance(self.v, resource_variable_ops.ResourceVariable)
