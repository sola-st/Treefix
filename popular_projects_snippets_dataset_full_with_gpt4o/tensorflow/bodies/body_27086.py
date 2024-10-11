# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
with self.assertRaises(errors.InvalidArgumentError):
    dataset = self._createSqlDataset(
        driver_name="sqlfake",
        query="SELECT first_name, last_name, motto FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.string, dtypes.string))
    self.assertDatasetProduces(dataset, expected_output=[])
