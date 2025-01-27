# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 27453
left_df = DataFrame({"animal": ["dog", "pig"], "max_speed": [40, 11]})
right_df = DataFrame({"animal": ["quetzal", "pig"], "max_speed": [80, 11]})
result = left_df.merge(right_df, on=["animal", "max_speed"], how=how)
if how == "right":
    expected = DataFrame({"animal": ["quetzal", "pig"], "max_speed": [80, 11]})
else:
    expected = DataFrame({"animal": ["dog", "pig"], "max_speed": [40, 11]})
tm.assert_frame_equal(result, expected)
