# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = dataset_ops.Dataset.from_tensors(0).map(lambda _: tf_value)
dataset_structure = structure.type_spec_from_value(dataset)
self.assertIsInstance(dataset_structure, dataset_ops.DatasetSpec)

self.assertTrue(
    structure.are_compatible(
        dataset_ops.get_structure(dataset), expected_element_structure))
self.assertEqual([dtypes.variant],
                 structure.get_flat_tensor_types(dataset_structure))
self.assertEqual([tensor_shape.TensorShape([])],
                 structure.get_flat_tensor_shapes(dataset_structure))

# Assert that the `Dataset` survives a round-trip via _from_tensor_list()
# and _to_tensor_list().
round_trip_dataset = dataset_structure._from_tensor_list(
    dataset_structure._to_tensor_list(dataset))

value = tf_value

if isinstance(value, dataset_ops.Dataset):
    self.assertDatasetsEqual(value, dataset.flat_map(lambda x: x))
elif isinstance(value, optional_ops.Optional):
    self.assertDatasetProduces(
        round_trip_dataset.map(lambda opt: opt.get_value()),
        [self.evaluate(value.get_value())],
        requires_initialization=True)
else:
    self.assertDatasetProduces(
        round_trip_dataset, [self.evaluate(tf_value)],
        requires_initialization=True)
