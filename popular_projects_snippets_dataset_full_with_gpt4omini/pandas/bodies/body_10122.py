# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
engine, raw = engine_and_raw

df = (
    DataFrame(
        {"A": date_range("20130101", periods=5, freq="s"), "B": range(5)}
    ).set_index("A")
    * 2
)
er = df.rolling(window=1)
r = df.rolling(window="1s")

result = r.apply(lambda x: 1, engine=engine, raw=raw)
expected = er.apply(lambda x: 1, engine=engine, raw=raw)
tm.assert_frame_equal(result, expected)
