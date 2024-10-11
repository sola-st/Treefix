# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
path = self._v1_single_metagraph_saved_model(False)
imported = load.load(path)
args, kwargs = (
    imported.signatures["serving_default"].structured_input_signature)
self.assertEqual(args, ())
self.assertAllEqual(
    kwargs, {"start": tensor_spec.TensorSpec(shape=None, name="start")})
