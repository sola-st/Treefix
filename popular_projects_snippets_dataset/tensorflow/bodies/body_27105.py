# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, brownie_points FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.uint8)))
# Min value of uint8
self.assertEqual((b"John", 0), self.evaluate(get_next()))
# Max value of uint8
self.assertEqual((b"Jane", 255), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
