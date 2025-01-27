# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, favorite_number FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.int32)))
# Max value of int32
self.assertEqual((b"John", 2147483647), self.evaluate(get_next()))
# Min value of int32
self.assertEqual((b"Jane", -2147483648), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
