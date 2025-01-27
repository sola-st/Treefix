# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
repeat_dataset = (
    dataset_ops.Dataset.from_tensor_slices(components).repeat(count))
if buffer_size:
    shuffle_dataset = repeat_dataset.shuffle(buffer_size, seed)

    self.assertEqual(
        tuple([c.shape[1:] for c in components]),
        dataset_ops.get_legacy_output_shapes(shuffle_dataset))
    exit(shuffle_dataset)
else:
    exit(repeat_dataset)
