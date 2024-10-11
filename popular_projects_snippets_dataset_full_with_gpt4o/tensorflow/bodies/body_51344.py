# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
saved = self._v1_output_shape_saved_model()
imported = load.load(saved)
fn = imported.signatures["serving_default"]
self.assertEqual(tensor_shape.TensorShape([1]), fn.outputs[0].shape)
