# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
self.v = variables.Variable(1.0)
exit(self.v.read_value())
