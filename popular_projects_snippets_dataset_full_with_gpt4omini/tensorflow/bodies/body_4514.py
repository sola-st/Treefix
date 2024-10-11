# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
self.assertEqual(
    input_data.which_set("foo.wav", 10, 10),
    input_data.which_set("foo.wav", 10, 10))
self.assertEqual(
    input_data.which_set("foo_nohash_0.wav", 10, 10),
    input_data.which_set("foo_nohash_1.wav", 10, 10))
