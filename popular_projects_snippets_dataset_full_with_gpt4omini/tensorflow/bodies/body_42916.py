# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
val = ragged_tensor.RaggedTensor.from_row_splits(values=[1],
                                                 row_splits=[0, 1])
with self.assertRaisesRegex(
    ValueError, "Structure had 2 atoms, but flat_sequence had 1 items."):
    nest.pack_sequence_as(val, [val], expand_composites=True)
