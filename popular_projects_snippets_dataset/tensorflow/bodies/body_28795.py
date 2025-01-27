# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/counter_test.py
dataset = dataset_ops.Dataset.counter(start, step)
self.assertEqual(
    [], dataset_ops.get_legacy_output_shapes(dataset).as_list())
self.assertEqual(dtypes.int64, dataset_ops.get_legacy_output_types(dataset))
get_next = self.getNext(dataset)
for expected in expected_output:
    self.assertEqual(expected, self.evaluate(get_next()))
