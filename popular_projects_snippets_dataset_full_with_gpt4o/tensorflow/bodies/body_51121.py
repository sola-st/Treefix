# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = module.Module()
initializer = lookup_ops.TextFileInitializer(
    self._vocab_path,
    key_dtype=dtypes.string,
    key_index=lookup_ops.TextFileIndex.WHOLE_LINE,
    value_dtype=dtypes.int64,
    value_index=lookup_ops.TextFileIndex.LINE_NUMBER)
table = lookup_ops.HashTable(initializer, default_value=-1)
root.table_user = def_function.function(
    table.lookup,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.string)])
root.table_user(constant_op.constant("gamma"))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
with self.assertRaisesRegexp(AssertionError, "HashTable"):
    save.save(root, save_dir)
