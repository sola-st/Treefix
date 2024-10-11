# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH#46252 custom formatting directives %l (ms) and %u (us)

# 3 digits
per = pd.period_range("2003-01-01 12:01:01.123", periods=2, freq="l")
formatted = per.format(date_format="%y %I:%M:%S (ms=%l us=%u ns=%n)")
assert formatted[0] == "03 12:01:01 (ms=123 us=123000 ns=123000000)"
assert formatted[1] == "03 12:01:01 (ms=124 us=124000 ns=124000000)"

# 6 digits
per = pd.period_range("2003-01-01 12:01:01.123456", periods=2, freq="u")
formatted = per.format(date_format="%y %I:%M:%S (ms=%l us=%u ns=%n)")
assert formatted[0] == "03 12:01:01 (ms=123 us=123456 ns=123456000)"
assert formatted[1] == "03 12:01:01 (ms=123 us=123457 ns=123457000)"

# 9 digits
per = pd.period_range("2003-01-01 12:01:01.123456789", periods=2, freq="n")
formatted = per.format(date_format="%y %I:%M:%S (ms=%l us=%u ns=%n)")
assert formatted[0] == "03 12:01:01 (ms=123 us=123456 ns=123456789)"
assert formatted[1] == "03 12:01:01 (ms=123 us=123456 ns=123456790)"
