# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
structure = "lots of letters"
flattened = nest.flatten(structure)
self.assertLen(flattened, 1)
unflattened = nest.pack_sequence_as("goodbye", flattened)
self.assertEqual(structure, unflattened)
