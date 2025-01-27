# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="SELECT students.first_name, state, motto FROM students "
        "INNER JOIN people "
        "ON students.first_name = people.first_name "
        "AND students.last_name = people.last_name",
        output_types=(dtypes.string, dtypes.string, dtypes.string)))

self.assertEqual((b"John", b"California", b"Hi!"),
                 self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
