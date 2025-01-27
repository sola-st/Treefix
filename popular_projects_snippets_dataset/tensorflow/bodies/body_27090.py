# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
get_next = self.getNext(
    self._createSqlDataset(
        query="INSERT INTO students (first_name, last_name, motto) "
        "VALUES ('Foo', 'Bar', 'Baz'), ('Fizz', 'Buzz', 'Fizzbuzz')",
        output_types=(dtypes.string, dtypes.string, dtypes.string)))
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(get_next())
