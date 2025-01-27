# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
dataset = dataset_ops.Dataset.from_tensors("xxx")
# decode_image results in a tensor of completely unknown shape (i.e. unknown
# rank)
dataset = dataset.map(image_ops.decode_image)
self.assertEqual([tensor_shape.TensorShape(None)],
                 nest.flatten(
                     dataset_ops.get_legacy_output_shapes(dataset)))
rebatched_dataset = distribute._LegacyRebatchDataset(
    dataset, num_replicas=4)
# Note that we are just testing the dataset shapes, not the actual output.
self.assertEqual(
    [tensor_shape.TensorShape(None)],
    nest.flatten(dataset_ops.get_legacy_output_shapes(rebatched_dataset)))
