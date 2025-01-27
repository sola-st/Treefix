# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH#46468 non-ascii char in input format string leads to wrong output

# Skip if locale cannot be set
if locale_str is not None and not tm.can_set_locale(locale_str, locale.LC_ALL):
    pytest.skip(f"Skipping as locale '{locale_str}' cannot be set on host.")

# Change locale temporarily for this test.
with tm.set_locale(locale_str, locale.LC_ALL) if locale_str else nullcontext():
    # Scalar
    per = pd.Period("2018-03-11 13:00", freq="H")
    assert per.strftime("%y é") == "18 é"

    # Index
    per = pd.period_range("2003-01-01 01:00:00", periods=2, freq="12h")
    formatted = per.format(date_format="%y é")
    assert formatted[0] == "03 é"
    assert formatted[1] == "03 é"
