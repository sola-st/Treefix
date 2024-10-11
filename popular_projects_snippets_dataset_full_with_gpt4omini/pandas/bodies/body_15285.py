# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH#48653
ser = Series({True: 1, False: 0})
with pytest.raises(KeyError, match="0"):
    ser.loc[0]
