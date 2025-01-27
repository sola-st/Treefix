# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def foo(a, b):
    del a
    del b

# Signatures must be either lists or tuples on their outermost levels.
signature = {'t1': tensor_spec.TensorSpec([], dtypes.float32)}
with self.assertRaisesRegex(
    TypeError, 'input_signature must be either a '
    'tuple or a list.*'):
    quarantine.defun_with_attributes(foo, input_signature=signature)
