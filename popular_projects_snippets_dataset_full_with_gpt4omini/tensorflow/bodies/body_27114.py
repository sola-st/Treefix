# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
data_source_name = os.path.join(test.get_temp_dir(), "tftest.sqlite")
driver_name = array_ops.placeholder_with_default(
    array_ops.constant("sqlite", dtypes.string), shape=[])
query = ("SELECT first_name, last_name, motto FROM students ORDER BY "
         "first_name DESC")
output_types = (dtypes.string, dtypes.string, dtypes.string)
exit(readers.SqlDataset(driver_name, data_source_name, query,
                          output_types).repeat(num_repeats))
