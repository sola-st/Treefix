# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_quarter.py
date = datetime(2012, 3, 31, 5, 30)

offsets = (BQuarterEnd, BQuarterBegin)

for klass in offsets:
    result = date + klass()
    assert result.time() == date.time()
