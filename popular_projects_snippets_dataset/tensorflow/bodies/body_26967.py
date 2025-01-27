# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
elements = [[[1]], [[2, 3]], [[4, 5, 6]]]
dataset = from_list.from_list(elements)
self.assertEqual(
    tensor_shape.Dimension(1),
    dataset_ops.get_legacy_output_shapes(dataset)[0])
self.assertDatasetProduces(dataset, expected_output=elements)
