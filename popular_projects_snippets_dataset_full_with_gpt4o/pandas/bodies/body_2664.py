# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_round.py
# GH#11885
df = DataFrame(
    {
        "col1": [1.1, 2.2, 3.3, 4.4],
        "col2": ["1", "a", "c", "f"],
        "col3": date_range("20111111", periods=4),
    }
)
round_0 = DataFrame(
    {
        "col1": [1.0, 2.0, 3.0, 4.0],
        "col2": ["1", "a", "c", "f"],
        "col3": date_range("20111111", periods=4),
    }
)
tm.assert_frame_equal(df.round(), round_0)
tm.assert_frame_equal(df.round(1), df)
tm.assert_frame_equal(df.round({"col1": 1}), df)
tm.assert_frame_equal(df.round({"col1": 0}), round_0)
tm.assert_frame_equal(df.round({"col1": 0, "col2": 1}), round_0)
tm.assert_frame_equal(df.round({"col3": 1}), df)
