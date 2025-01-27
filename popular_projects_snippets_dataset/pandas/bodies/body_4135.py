# Extracted from ./data/repos/pandas/pandas/tests/frame/test_iteration.py
for i, tup in enumerate(float_frame.itertuples()):
    ser = DataFrame._constructor_sliced(tup[1:])
    ser.name = tup[0]
    expected = float_frame.iloc[i, :].reset_index(drop=True)
    tm.assert_series_equal(ser, expected)

df = DataFrame(
    {"floats": np.random.randn(5), "ints": range(5)}, columns=["floats", "ints"]
)

for tup in df.itertuples(index=False):
    assert isinstance(tup[1], int)

df = DataFrame(data={"a": [1, 2, 3], "b": [4, 5, 6]})
dfaa = df[["a", "a"]]

assert list(dfaa.itertuples()) == [(0, 1, 1), (1, 2, 2), (2, 3, 3)]

# repr with int on 32-bit/windows
if not (is_platform_windows() or not IS64):
    assert (
        repr(list(df.itertuples(name=None)))
        == "[(0, 1, 4), (1, 2, 5), (2, 3, 6)]"
    )

tup = next(df.itertuples(name="TestName"))
assert tup._fields == ("Index", "a", "b")
assert (tup.Index, tup.a, tup.b) == tup
assert type(tup).__name__ == "TestName"

df.columns = ["def", "return"]
tup2 = next(df.itertuples(name="TestName"))
assert tup2 == (0, 1, 4)
assert tup2._fields == ("Index", "_1", "_2")

df3 = DataFrame({"f" + str(i): [i] for i in range(1024)})
# will raise SyntaxError if trying to create namedtuple
tup3 = next(df3.itertuples())
assert isinstance(tup3, tuple)
assert hasattr(tup3, "_fields")

# GH#28282
df_254_columns = DataFrame([{f"foo_{i}": f"bar_{i}" for i in range(254)}])
result_254_columns = next(df_254_columns.itertuples(index=False))
assert isinstance(result_254_columns, tuple)
assert hasattr(result_254_columns, "_fields")

df_255_columns = DataFrame([{f"foo_{i}": f"bar_{i}" for i in range(255)}])
result_255_columns = next(df_255_columns.itertuples(index=False))
assert isinstance(result_255_columns, tuple)
assert hasattr(result_255_columns, "_fields")
