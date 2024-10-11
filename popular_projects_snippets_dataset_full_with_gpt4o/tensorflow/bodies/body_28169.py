# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
dataset = dataset_ops.Dataset.range(8).batch(4, drop_remainder=True)
rebatched_dataset = dataset_ops.rebatch(
    dataset, batch_sizes=[0, 1], drop_remainder=drop_remainder)

expected_shapes = [[None]]
self.assertEqual(expected_shapes, _flat_shapes(rebatched_dataset))

# We have an extra element at the end because if the desired batch size is
# zero, then we never read any inputs from the input_dataset at all, so we
# will keep producting empty outputs until we reach a non zero desired batch
# size split.
expected_output = [[], [0], [], [1], [], [2], [], [3], [], [4], [], [5], [],
                   [6], [], [7], []]
self.assertDatasetProduces(rebatched_dataset, expected_output)
