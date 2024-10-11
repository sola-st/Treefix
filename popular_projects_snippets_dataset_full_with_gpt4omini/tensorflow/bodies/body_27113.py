# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
dataset = self._createSqlDataset(
    query="SELECT * FROM data", output_types=(dtypes.int32))
dataset = dataset.map(lambda x: array_ops.identity(x))
get_next = self.getNext(dataset.batch(2))
self.assertAllEqual(self.evaluate(get_next()), [0, 1])
self.assertAllEqual(self.evaluate(get_next()), [2])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
