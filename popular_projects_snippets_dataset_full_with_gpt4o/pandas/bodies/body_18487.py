# Extracted from ./data/repos/pandas/pandas/tests/test_errors.py
from pandas import errors

err = getattr(errors, exc)
assert err is not None

# check that we can raise on them

msg = "^$"

with pytest.raises(err, match=msg):
    raise err()
