# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
first_path = self._v1_asset_saved_model(clear_shared_name=False)
imported = load.load(first_path)
self.evaluate(lookup_ops.tables_initializer())
fn = imported.signatures["serving_default"]
self.assertAllClose({"output": [2, 0]},
                    fn(start=constant_op.constant(["gamma", "alpha"])))
second_path = os.path.join(self.get_temp_dir(), "saved_model",
                           str(ops.uid()))
save.save(imported, second_path, signatures=imported.signatures)
shutil.rmtree(first_path)
del ops.get_collection_ref(ops.GraphKeys.TABLE_INITIALIZERS)[:]
second_import = load.load(second_path)
self.evaluate(lookup_ops.tables_initializer())
fn = second_import.signatures["serving_default"]
self.assertAllClose({"output": [2, 0]},
                    fn(start=constant_op.constant(["gamma", "alpha"])))

third_path = os.path.join(self.get_temp_dir(), "saved_model",
                          str(ops.uid()))
save.save(second_import, third_path, signatures=second_import.signatures)
shutil.rmtree(second_path)
del ops.get_collection_ref(ops.GraphKeys.TABLE_INITIALIZERS)[:]
third_import = load.load(third_path)
self.evaluate(lookup_ops.tables_initializer())
fn = third_import.signatures["serving_default"]
self.assertAllClose({"output": [2, 0]},
                    fn(start=constant_op.constant(["gamma", "alpha"])))
