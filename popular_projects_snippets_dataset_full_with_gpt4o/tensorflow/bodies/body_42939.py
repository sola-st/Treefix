# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
seq = _CustomSequenceThatRaisesException()
with self.assertRaisesRegex(ValueError, "Cannot get item"):
    nest.flatten(seq)
