# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
self.assertEqual(set(dict_tensors.keys()), set(expected_tensors.keys()))

for k, v in sorted(dict_tensors.items()):
    expected_v = expected_tensors[k]
    self.assertValuesEqual(expected_v, v)
