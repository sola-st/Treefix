# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_asfreq.py
pi1 = period_range(freq="A", start="1/1/2001", end="1/1/2001")
pi2 = period_range(freq="Q", start="1/1/2001", end="1/1/2001")
pi3 = period_range(freq="M", start="1/1/2001", end="1/1/2001")
pi4 = period_range(freq="D", start="1/1/2001", end="1/1/2001")
pi5 = period_range(freq="H", start="1/1/2001", end="1/1/2001 00:00")
pi6 = period_range(freq="Min", start="1/1/2001", end="1/1/2001 00:00")
pi7 = period_range(freq="S", start="1/1/2001", end="1/1/2001 00:00:00")

assert pi1.asfreq("Q", "S") == pi2
assert pi1.asfreq("Q", "s") == pi2
assert pi1.asfreq("M", "start") == pi3
assert pi1.asfreq("D", "StarT") == pi4
assert pi1.asfreq("H", "beGIN") == pi5
assert pi1.asfreq("Min", "S") == pi6
assert pi1.asfreq("S", "S") == pi7

assert pi2.asfreq("A", "S") == pi1
assert pi2.asfreq("M", "S") == pi3
assert pi2.asfreq("D", "S") == pi4
assert pi2.asfreq("H", "S") == pi5
assert pi2.asfreq("Min", "S") == pi6
assert pi2.asfreq("S", "S") == pi7

assert pi3.asfreq("A", "S") == pi1
assert pi3.asfreq("Q", "S") == pi2
assert pi3.asfreq("D", "S") == pi4
assert pi3.asfreq("H", "S") == pi5
assert pi3.asfreq("Min", "S") == pi6
assert pi3.asfreq("S", "S") == pi7

assert pi4.asfreq("A", "S") == pi1
assert pi4.asfreq("Q", "S") == pi2
assert pi4.asfreq("M", "S") == pi3
assert pi4.asfreq("H", "S") == pi5
assert pi4.asfreq("Min", "S") == pi6
assert pi4.asfreq("S", "S") == pi7

assert pi5.asfreq("A", "S") == pi1
assert pi5.asfreq("Q", "S") == pi2
assert pi5.asfreq("M", "S") == pi3
assert pi5.asfreq("D", "S") == pi4
assert pi5.asfreq("Min", "S") == pi6
assert pi5.asfreq("S", "S") == pi7

assert pi6.asfreq("A", "S") == pi1
assert pi6.asfreq("Q", "S") == pi2
assert pi6.asfreq("M", "S") == pi3
assert pi6.asfreq("D", "S") == pi4
assert pi6.asfreq("H", "S") == pi5
assert pi6.asfreq("S", "S") == pi7

assert pi7.asfreq("A", "S") == pi1
assert pi7.asfreq("Q", "S") == pi2
assert pi7.asfreq("M", "S") == pi3
assert pi7.asfreq("D", "S") == pi4
assert pi7.asfreq("H", "S") == pi5
assert pi7.asfreq("Min", "S") == pi6

msg = "How must be one of S or E"
with pytest.raises(ValueError, match=msg):
    pi7.asfreq("T", "foo")
result1 = pi1.asfreq("3M")
result2 = pi1.asfreq("M")
expected = period_range(freq="M", start="2001-12", end="2001-12")
tm.assert_numpy_array_equal(result1.asi8, expected.asi8)
assert result1.freqstr == "3M"
tm.assert_numpy_array_equal(result2.asi8, expected.asi8)
assert result2.freqstr == "M"
