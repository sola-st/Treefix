# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
self.assertEqual(
    nest.flatten_with_joined_string_paths(inputs, separator="/"),
    expected)
