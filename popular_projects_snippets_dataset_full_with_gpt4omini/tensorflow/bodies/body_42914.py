# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
with self.assertRaisesRegex(TypeError, self.bad_pack_pattern):
    nest.pack_sequence_as("hi", "bye")
