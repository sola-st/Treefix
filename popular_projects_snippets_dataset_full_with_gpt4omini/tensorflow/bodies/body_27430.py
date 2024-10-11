# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
get_next = self.getNext(dataset)

for expected_features in self._next_expected_batch(
    expected_output,
    expected_keys,
    batch_size,
    num_epochs,
):
    actual_features = self.evaluate(get_next())

    if label_name is not None:
        expected_labels = expected_features.pop(label_name)
        self.assertAllEqual(expected_labels, actual_features[1])
        actual_features = actual_features[0]

    for k in expected_features.keys():
        # Compare features
        self.assertAllEqual(expected_features[k], actual_features[k])

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
