# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH#46319 locale-specific directive leads to non-utf8 c strftime char* result

# Skip if locale cannot be set
if locale_str is not None and not tm.can_set_locale(locale_str, locale.LC_ALL):
    pytest.skip(f"Skipping as locale '{locale_str}' cannot be set on host.")

# Change locale temporarily for this test.
with tm.set_locale(locale_str, locale.LC_ALL) if locale_str else nullcontext():
    # Get locale-specific reference
    am_local, pm_local = get_local_am_pm()

    # Scalar
    per = pd.Period("2018-03-11 13:00", freq="H")
    assert per.strftime("%p") == pm_local

    # Index
    per = pd.period_range("2003-01-01 01:00:00", periods=2, freq="12h")
    formatted = per.format(date_format="%y %I:%M:%S%p")
    assert formatted[0] == f"03 01:00:00{am_local}"
    assert formatted[1] == f"03 01:00:00{pm_local}"
