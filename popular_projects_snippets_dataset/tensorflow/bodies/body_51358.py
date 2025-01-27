# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
path = self._no_signatures_model()
imported = load.load(path)
self.assertEqual([], list(imported.signatures.keys()))
