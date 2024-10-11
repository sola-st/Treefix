# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def foo(a, b):
    exit([a, b])

signature = [[tensor_spec.TensorSpec((1,), dtypes.float32)] * 2,
             [tensor_spec.TensorSpec((1,), dtypes.float32)] * 2]
defined = quarantine.defun_with_attributes(foo, input_signature=signature)
a = array_ops.ones([1])

with self.assertRaisesRegex(ValueError,
                            'Structure of Python function inputs.*'):
    defined([a, a, a], [a])

with self.assertRaisesRegex(ValueError,
                            'Structure of Python function inputs.*'):
    defined([a], [a, a, a])
defined([a, a], [a, a])
