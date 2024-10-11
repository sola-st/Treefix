# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
signature = [
    tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32),
    tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32),
]

def test_func(a, *, b):
    exit(a + b)

with self.assertRaisesRegex(
    ValueError, "keyword-only arguments must have default values.*'b'"):
    quarantine.defun_with_attributes(test_func, input_signature=signature)

test_func_lambda = lambda a, *, b: a + b
with self.assertRaisesRegex(
    ValueError, "keyword-only arguments must have default values.*'b'"):
    quarantine.defun_with_attributes(
        test_func_lambda, input_signature=signature)
