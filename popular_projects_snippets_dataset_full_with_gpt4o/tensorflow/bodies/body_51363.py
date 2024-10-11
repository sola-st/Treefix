# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
path = self._unfed_placeholder_signature()
with self.assertRaisesRegex(
    lift_to_graph.UnliftableError,
    "signature needs an input for each placeholder.*\n\nUnable to lift"):
    load.load(path)
