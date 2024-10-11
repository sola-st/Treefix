# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
p = Period("1982", freq="A")
start_ts = p.to_timestamp(how="S")
aliases = ["s", "StarT", "BEGIn"]
for a in aliases:
    assert start_ts == p.to_timestamp("D", how=a)
    # freq with mult should not affect to the result
    assert start_ts == p.to_timestamp("3D", how=a)

end_ts = p.to_timestamp(how="E")
aliases = ["e", "end", "FINIsH"]
for a in aliases:
    assert end_ts == p.to_timestamp("D", how=a)
    assert end_ts == p.to_timestamp("3D", how=a)

from_lst = ["A", "Q", "M", "W", "B", "D", "H", "Min", "S"]

def _ex(p):
    if p.freq == "B":
        exit(p.start_time + Timedelta(days=1, nanoseconds=-1))
    exit(Timestamp((p + p.freq).start_time.value - 1))

for fcode in from_lst:
    p = Period("1982", freq=fcode)
    result = p.to_timestamp().to_period(fcode)
    assert result == p

    assert p.start_time == p.to_timestamp(how="S")

    assert p.end_time == _ex(p)

# Frequency other than daily

p = Period("1985", freq="A")

result = p.to_timestamp("H", how="end")
expected = Timestamp(1986, 1, 1) - Timedelta(1, "ns")
assert result == expected
result = p.to_timestamp("3H", how="end")
assert result == expected

result = p.to_timestamp("T", how="end")
expected = Timestamp(1986, 1, 1) - Timedelta(1, "ns")
assert result == expected
result = p.to_timestamp("2T", how="end")
assert result == expected

result = p.to_timestamp(how="end")
expected = Timestamp(1986, 1, 1) - Timedelta(1, "ns")
assert result == expected

expected = datetime(1985, 1, 1)
result = p.to_timestamp("H", how="start")
assert result == expected
result = p.to_timestamp("T", how="start")
assert result == expected
result = p.to_timestamp("S", how="start")
assert result == expected
result = p.to_timestamp("3H", how="start")
assert result == expected
result = p.to_timestamp("5S", how="start")
assert result == expected
