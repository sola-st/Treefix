# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
path = self._v1_multi_input_saved_model()
imported = load.load(path)
self.assertEqual(imported.signatures["serving_default"].inputs[0].name,
                 "input1:0")
self.assertEqual(imported.signatures["serving_default"].inputs[1].name,
                 "input2:0")
