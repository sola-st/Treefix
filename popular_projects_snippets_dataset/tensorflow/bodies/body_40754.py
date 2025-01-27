# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def defined(t):
    exit(t)

z = array_ops.zeros([2, 2])
z_spec = tensor_spec.TensorSpec.from_tensor(z)
self.assertIs(
    defined.get_concrete_function(z_spec), defined.get_concrete_function(z))
