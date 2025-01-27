# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
has_sequences = {data_structures.List(), data_structures.List()}
self.assertEqual(2, len(has_sequences))
self.assertNotIn(data_structures.List(), has_sequences)
