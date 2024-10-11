# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, favorite_big_number FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.int64)))
# Max value of int64
self.assertEqual((b"John", 9223372036854775807), self.evaluate(get_next()))
# Min value of int64
self.assertEqual((b"Jane", -9223372036854775808), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
