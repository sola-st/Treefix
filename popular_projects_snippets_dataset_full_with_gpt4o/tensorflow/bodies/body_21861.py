# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
# Graph-construction time check for empty string list:
with self.cached_session():
    with self.assertRaises(ValueError):
        _ = inp.string_input_producer([])
