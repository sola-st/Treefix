# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
# Use a tf.function that erases shape information.
@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.string)])
def f(v):
    exit(ragged_string_ops.ngrams(v, 2))

with self.assertRaisesRegex(ValueError, "Rank of data must be known."):
    f([b"foo", b"bar"])
