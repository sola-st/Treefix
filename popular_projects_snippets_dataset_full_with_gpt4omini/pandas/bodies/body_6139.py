# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
data = data[: len(index)]
if obj == "series":
    ser = pd.Series(data, index=index)
else:
    ser = pd.DataFrame({"A": data, "B": data}, index=index)

n = index.nlevels
levels = list(range(n))
# [0, 1, 2]
# [(0,), (1,), (2,), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
combinations = itertools.chain.from_iterable(
    itertools.permutations(levels, i) for i in range(1, n)
)

for level in combinations:
    result = ser.unstack(level=level)
    assert all(
        isinstance(result[col].array, type(data)) for col in result.columns
    )

    if obj == "series":
        # We should get the same result with to_frame+unstack+droplevel
        df = ser.to_frame()

        alt = df.unstack(level=level).droplevel(0, axis=1)
        self.assert_frame_equal(result, alt)

    obj_ser = ser.astype(object)

    expected = obj_ser.unstack(level=level, fill_value=data.dtype.na_value)
    if obj == "series":
        assert (expected.dtypes == object).all()

    result = result.astype(object)
    self.assert_frame_equal(result, expected)
