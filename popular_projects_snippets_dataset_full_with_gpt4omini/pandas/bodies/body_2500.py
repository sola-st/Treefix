# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#12533
result = float_frame[lambda x: "A"]
expected = float_frame.loc[:, "A"]
tm.assert_series_equal(result, expected)

result = float_frame[lambda x: ["A", "B"]]
expected = float_frame.loc[:, ["A", "B"]]
tm.assert_frame_equal(result, float_frame.loc[:, ["A", "B"]])

df = float_frame[:3]
result = df[lambda x: [True, False, True]]
expected = float_frame.iloc[[0, 2], :]
tm.assert_frame_equal(result, expected)
