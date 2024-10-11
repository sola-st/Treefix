# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# PR8618 and issue 8015
frame = mframe

msg = "You have to supply one of 'by' and 'level'"
with pytest.raises(TypeError, match=msg):
    frame.groupby()

msg = "You have to supply one of 'by' and 'level'"
with pytest.raises(TypeError, match=msg):
    frame.groupby(by=None, level=None)
