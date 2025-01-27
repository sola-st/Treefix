# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, last_name, victories FROM townspeople "
        "ORDER BY first_name",
        output_types=(dtypes.string, dtypes.string, dtypes.float64)))
self.assertEqual((b"George", b"Washington", 20.0),
                 self.evaluate(get_next()))
self.assertEqual((b"John", b"Adams", -19.95), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
