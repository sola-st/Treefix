# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT desk_number, favorite_negative_number FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.int8, dtypes.int8)))
self.assertEqual((9, -2), self.evaluate(get_next()))
# Max and min values of int8
self.assertEqual((127, -128), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
