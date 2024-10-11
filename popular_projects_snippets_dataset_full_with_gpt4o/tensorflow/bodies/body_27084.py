# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, last_name, motto FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.string, dtypes.string)))
self.assertEqual((b"John", b"Doe", b"Hi!"), self.evaluate(get_next()))
self.assertEqual((b"Jane", b"Moe", b"Hi again!"), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, last_name, state FROM people "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.string, dtypes.string)))
self.assertEqual((b"John", b"Doe", b"California"),
                 self.evaluate(get_next()))
self.assertEqual((b"Benjamin", b"Franklin", b"Pennsylvania"),
                 self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
