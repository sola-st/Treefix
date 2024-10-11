# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
start_data, expected_result = expected

start_dataframe = DataFrame({"foo": start_data})
start_dataframe.loc[start_dataframe["foo"] == start_dataframe["foo"][0]] = None

expected_dataframe = DataFrame({"foo": expected_result})
tm.assert_frame_equal(start_dataframe, expected_dataframe)
