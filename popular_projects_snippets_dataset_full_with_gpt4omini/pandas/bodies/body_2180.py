# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# dayfirst is essentially broken

# The msg here is not important since it isn't actually raised yet.
msg = "Invalid date specified"
with pytest.raises(ValueError, match=msg):
    # if dayfirst is respected, then this would parse as month=13, which
    #  would raise
    with tm.assert_produces_warning(UserWarning, match="Provide format"):
        to_datetime("01-13-2012", dayfirst=True, cache=cache)
