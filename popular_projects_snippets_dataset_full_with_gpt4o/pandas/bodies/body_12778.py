# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH #43831
data = {"a": [1, 2], "b": {"b_1": 2, "b_2": (3, 4)}}
result = json_normalize(data, sep="__")
expected = DataFrame([[[1, 2], 2, (3, 4)]], columns=["a", "b__b_1", "b__b_2"])
tm.assert_frame_equal(result, expected)
