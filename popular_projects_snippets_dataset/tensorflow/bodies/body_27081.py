# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
for _ in range(2):  # Run twice to verify statelessness of db operations.
    dataset = self._createSqlDataset(
        query="SELECT first_name, last_name, motto FROM students "
        "ORDER BY first_name DESC",
        output_types=(dtypes.string, dtypes.string, dtypes.string),
        num_repeats=2)
    self.assertDatasetProduces(
        dataset,
        expected_output=[(b"John", b"Doe", b"Hi!"),
                         (b"Jane", b"Moe", b"Hi again!")] * 2,
        num_test_iterations=2)
