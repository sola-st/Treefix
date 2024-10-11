# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, registration_complete FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.bool)))
self.assertEqual((b"John", True), self.evaluate(get_next()))
self.assertEqual((b"Jane", False), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
