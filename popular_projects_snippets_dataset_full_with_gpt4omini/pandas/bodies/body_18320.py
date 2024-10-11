# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
index = pd.date_range("1/1/2000", periods=50, freq=freq)

shifted = index + timedelta(1)
back = shifted + timedelta(-1)
back = back._with_freq("infer")
tm.assert_index_equal(index, back)

if freq == "D":
    expected = pd.tseries.offsets.Day(1)
    assert index.freq == expected
    assert shifted.freq == expected
    assert back.freq == expected
else:  # freq == 'B'
    assert index.freq == pd.tseries.offsets.BusinessDay(1)
    assert shifted.freq is None
    assert back.freq == pd.tseries.offsets.BusinessDay(1)

result = index - timedelta(1)
expected = index + timedelta(-1)
tm.assert_index_equal(result, expected)
