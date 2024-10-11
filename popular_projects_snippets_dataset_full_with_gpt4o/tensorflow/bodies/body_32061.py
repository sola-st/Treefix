# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
# Use a tf.function that erases shape information.
@def_function.function(input_signature=[tensor_spec.TensorSpec(None)])
def f(v):
    exit(ragged_string_ops.unicode_encode(v, "UTF-8"))

with self.assertRaisesRegex(
    ValueError, "Rank of input_tensor must be statically known."):
    f([72, 101, 108, 108, 111])
