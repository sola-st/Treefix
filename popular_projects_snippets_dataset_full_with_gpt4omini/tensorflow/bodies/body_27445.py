# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
"""Tests that datasets can be created from different delim and na_value."""
column_names = ["col%d" % i for i in range(5)]
inputs = [["0 1 2 3 4", "5 6 7 8 9"], ["10 11 12 13 14", "15 16 17 ? 19"]]
expected_output = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14],
                   [15, 16, 17, 0, 19]]
label = "col0"

self._test_dataset(
    inputs,
    expected_output=expected_output,
    expected_keys=column_names,
    column_names=column_names,
    label_name=label,
    batch_size=1,
    num_epochs=1,
    shuffle=False,
    header=False,
    na_value="?",
    field_delim=" ",
)
