# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, last_name, motto FROM students "
        "WHERE first_name = 'Nonexistent'",
        output_types=(dtypes.string, dtypes.string, dtypes.string)))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
