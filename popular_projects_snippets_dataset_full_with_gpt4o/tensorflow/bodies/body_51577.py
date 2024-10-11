# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
# Test with StaticHashTable, which has a _initializer attribute that tracks
# the Asset vocab table.

class MyLookupModel(autotrackable.AutoTrackable):

    def __init__(self, vocab_file):
        vocab_initializer = lookup_ops.TextFileInitializer(
            vocab_file,
            key_dtype=dtypes.string,
            key_index=lookup_ops.TextFileIndex.WHOLE_LINE,
            value_dtype=dtypes.int64,
            value_index=lookup_ops.TextFileIndex.LINE_NUMBER,
        )
        self._vocab_table = lookup_ops.StaticHashTable(
            vocab_initializer, default_value=-1
        )

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec((None,), dtypes.string)]
    )
    def __call__(self, inputs):
        exit(self._vocab_table.lookup(inputs))

vocab_file = self._make_asset("\n".join(["a", "b", "c", "d"]))
root = MyLookupModel(vocab_file)
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
file_io.delete_file(vocab_file)
self.assertAllEqual(imported(constant_op.constant(["d", "b"])), [3, 1])
