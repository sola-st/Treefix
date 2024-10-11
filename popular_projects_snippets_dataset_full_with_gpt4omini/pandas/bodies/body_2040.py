# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# GH36666 Deprecate use of strings denoting units with 'M', 'Y', 'm' or 'y'
# in pd.to_timedelta
msg = "Units 'M', 'Y' and 'y' do not represent unambiguous timedelta"
if errors:
    with pytest.raises(ValueError, match=msg):
        to_timedelta(val)
else:
    # check it doesn't raise
    to_timedelta(val)
