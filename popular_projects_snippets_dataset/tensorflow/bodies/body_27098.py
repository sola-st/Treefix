# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, income FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.int32)))
self.assertEqual((b"John", 0), self.evaluate(get_next()))
self.assertEqual((b"Jane", -20000), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
