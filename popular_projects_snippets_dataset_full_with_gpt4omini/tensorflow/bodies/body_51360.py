# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
path = self._signature_with_no_inputs()
imported = load.load(path)
self.assertEqual([2], imported.signatures["key"]()["value"].shape)
