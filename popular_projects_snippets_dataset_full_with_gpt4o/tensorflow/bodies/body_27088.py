# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELEmispellECT first_name, last_name, motto FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.string, dtypes.string)))
with self.assertRaises(errors.UnknownError):
    self.evaluate(get_next())
