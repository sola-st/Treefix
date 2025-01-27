# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
has_sequences = set([data_structures._TupleWrapper(),
                     data_structures._TupleWrapper()])
self.assertLen(has_sequences, 1)
self.assertIn(data_structures._TupleWrapper(), has_sequences)
