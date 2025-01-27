# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
initializer = lookup_ops.TextFileInitializer(
    self._vocab_path,
    key_dtype=dtypes.string,
    key_index=lookup_ops.TextFileIndex.WHOLE_LINE,
    value_dtype=dtypes.int64,
    value_index=lookup_ops.TextFileIndex.LINE_NUMBER)
root = checkpoint.Checkpoint(
    table=lookup_ops.HashTable(initializer, default_value=-1))
root.table_user = def_function.function(
    root.table.lookup,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.string)])
self.assertEqual(
    2, self.evaluate(root.table_user(constant_op.constant("gamma"))))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, save_dir)
file_io.delete_file(self._vocab_path)
self.assertAllClose({"output_0": [2, 0]},
                    _import_and_infer(save_dir,
                                      {"keys": ["gamma", "alpha"]}))
second_dir = os.path.join(self.get_temp_dir(), "second_dir")
# Asset paths should track the location the SavedModel is loaded from.
file_io.rename(save_dir, second_dir)
self.assertAllClose({"output_0": [2, 1]},
                    _import_and_infer(second_dir,
                                      {"keys": ["gamma", "beta"]}))
