# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH#34703
edate = datetime(2000, 1, 1)
with pytest.raises(TypeError, match="pass as a string instead"):
    date_range(end=edate, freq=("D", 5), periods=20)
