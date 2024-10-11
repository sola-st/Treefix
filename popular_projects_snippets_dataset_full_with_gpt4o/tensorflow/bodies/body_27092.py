# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, income, favorite_negative_number "
        "FROM students "
        "WHERE first_name = 'John' ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.int8, dtypes.int8)))
self.assertEqual((b"John", 0, -2), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
