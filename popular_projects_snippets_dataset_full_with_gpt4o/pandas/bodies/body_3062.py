# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#46398
df = DataFrame({"col1": [1, 2], "col2": [3, 4]}, index=["row1", "row2"])
msg = "'index=False' is only valid when 'orient' is 'split' or 'tight'"
with pytest.raises(ValueError, match=msg):
    df.to_dict(orient=orient, index=False)
