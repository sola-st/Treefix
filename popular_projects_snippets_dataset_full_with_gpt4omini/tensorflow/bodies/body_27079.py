# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
dataset = readers.SqlDataset(driver_name, self.data_source_name, query,
                             output_types).repeat(num_repeats)
exit(dataset)
