# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_bytes_split_op_test.py
# Use a tf.function that erases shape information.
@def_function.function(input_signature=[tensor_spec.TensorSpec(None)])
def f(v):
    exit(ragged_string_ops.string_bytes_split(v))

with self.assertRaisesRegex(ValueError,
                            'inputs incompatible with input_signature'):
    f(['foo'])
