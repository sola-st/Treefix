# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
"""Tests that datasets can be created when no defaults are specified.

    Tests on a deliberately tricky file.
    """
column_names = ["col%d" % i for i in range(5)]
str_int32_max = str(2**33)
inputs = [[
    ",".join(x for x in column_names),
    ",,,,",
    "0,0,0.0,0.0,0.0",
    "0,%s,2.0,3e50,rabbit" % str_int32_max,
    ",,,,",
]]
expected_output = [[0, 0, 0, 0, b""], [0, 0, 0, 0, b"0.0"],
                   [0, 2**33, 2.0, 3e50, b"rabbit"], [0, 0, 0, 0, b""]]
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
    header=True,
)
