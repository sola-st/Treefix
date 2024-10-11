# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH22468
# Don't raise ValueError when a column name is a substring
# of a stubname that's been passed as a string
wide_data = {
    "node_id": {0: 0, 1: 1, 2: 2, 3: 3, 4: 4},
    "A": {0: 0.80, 1: 0.0, 2: 0.25, 3: 1.0, 4: 0.81},
    "PA0": {0: 0.74, 1: 0.56, 2: 0.56, 3: 0.98, 4: 0.6},
    "PA1": {0: 0.77, 1: 0.64, 2: 0.52, 3: 0.98, 4: 0.67},
    "PA3": {0: 0.34, 1: 0.70, 2: 0.52, 3: 0.98, 4: 0.67},
}
wide_df = DataFrame.from_dict(wide_data)
expected = wide_to_long(wide_df, stubnames=["PA"], i=["node_id", "A"], j="time")
result = wide_to_long(wide_df, stubnames="PA", i=["node_id", "A"], j="time")
tm.assert_frame_equal(result, expected)
