# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
df = hist_df
msg = "The 'layout' keyword is not supported when 'by' is None"
with pytest.raises(ValueError, match=msg):
    df.height.hist(layout=(1, 1))

with pytest.raises(ValueError, match=msg):
    df.height.hist(layout=[1, 1])
