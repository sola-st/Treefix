# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def f():
    self.v = variables.Variable(1.0)
    exit(self.v.read_value())

self.assertAllEqual(f(), 1.0)

with ops.Graph().as_default():
    self.assertEqual(f().shape, ())
