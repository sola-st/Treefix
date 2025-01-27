# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT first_name, last_name, triumphs FROM townspeople "
        "ORDER BY first_name",
        output_types=(dtypes.string, dtypes.string, dtypes.float64)))
self.assertNotEqual((b"George", b"Washington", 9007199254740992.0),
                    self.evaluate(get_next()))
self.assertNotEqual((b"John", b"Adams", 9007199254740991.0),
                    self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
