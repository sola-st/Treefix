# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_formats.py
dr = pd.date_range(start="1/1/2012", periods=1)
repr(dr)

dr = pd.date_range(start="1/1/2012", periods=2)
repr(dr)

dr = pd.date_range(start="1/1/2012", periods=3)
repr(dr)
