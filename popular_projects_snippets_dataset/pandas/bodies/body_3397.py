# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH: 16784
columns_values_map = {"positive": {"正面": 1, "中立": 1, "负面": 0}}
df1 = DataFrame({"positive": np.ones(3)})
result = df1.replace(columns_values_map)
expected = DataFrame({"positive": np.ones(3)})
tm.assert_frame_equal(result, expected)
