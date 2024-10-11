# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_cardinality_test.py
dataset = dataset_ops.Dataset.range(num_elements)
dataset = dataset.apply(
    cardinality.assert_cardinality(asserted_cardinality))
get_next = self.getNext(dataset)
with self.assertRaisesRegex(errors.FailedPreconditionError, expected_error):
    while True:
        self.evaluate(get_next())
