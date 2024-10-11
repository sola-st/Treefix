# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
fourth_path = self._v1_asset_saved_model(clear_shared_name=True)
fourth_import = load.load(fourth_path)
self.evaluate(lookup_ops.tables_initializer())
fn = fourth_import.signatures["serving_default"]
self.assertAllClose({"output": [2, 0]},
                    fn(start=constant_op.constant(["gamma", "alpha"])))
