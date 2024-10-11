# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#353
vals = Series(tm.rands_array(5, 10))
result = "foo_" + vals
expected = vals.map(lambda x: "foo_" + x)
tm.assert_series_equal(result, expected)

frame = pd.DataFrame({"vals": vals})
result = "foo_" + frame
expected = pd.DataFrame({"vals": vals.map(lambda x: "foo_" + x)})
tm.assert_frame_equal(result, expected)

ts = tm.makeTimeSeries()
ts.name = "ts"

# really raise this time
fix_now = fixed_now_ts.to_pydatetime()
msg = "|".join(
    [
        "unsupported operand type",
        # wrong error message, see https://github.com/numpy/numpy/issues/18832
        "Concatenation operation",
    ]
)
with pytest.raises(TypeError, match=msg):
    fix_now + ts

with pytest.raises(TypeError, match=msg):
    ts + fix_now
