# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
saved = self._v1_single_metagraph_saved_model(use_resource=False)
imported = load.load(saved)
fn = imported.signatures["serving_default"]
self.evaluate(lookup_ops.tables_initializer())
self.evaluate(ops.get_collection("saved_model_initializers"))
self.assertEqual(
    6., self.evaluate(fn(start=constant_op.constant(2.))["output"]))
