# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
elements = [(1, 2), (3, 4)]
dataset = from_list.from_list(elements)
self.assertEqual(
    [np.shape(c) for c in elements[0]],
    [shape for shape in dataset_ops.get_legacy_output_shapes(dataset)])
self.assertDatasetProduces(dataset, expected_output=elements)
