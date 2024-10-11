# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
# GH 46683
p = PeriodIndex(["2022-04-06", "2022-04-07"], freq="D")
df = DataFrame(index=p)
assert df.to_json() == "{}"
