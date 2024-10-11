# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# masked int promoted to float
mat = ma.masked_all((2, 3), dtype=int)
# 2-D input
frame = DataFrame(mat, columns=["A", "B", "C"], index=[1, 2])

assert len(frame.index) == 2
assert len(frame.columns) == 3
assert np.all(~np.asarray(frame == frame))

# cast type
frame = DataFrame(mat, columns=["A", "B", "C"], index=[1, 2], dtype=np.float64)
assert frame.values.dtype == np.float64

# Check non-masked values
mat2 = ma.copy(mat)
mat2[0, 0] = 1
mat2[1, 2] = 2
frame = DataFrame(mat2, columns=["A", "B", "C"], index=[1, 2])
assert 1 == frame["A"][1]
assert 2 == frame["C"][2]

# masked np.datetime64 stays (use NaT as null)
mat = ma.masked_all((2, 3), dtype="M8[ns]")
# 2-D input
frame = DataFrame(mat, columns=["A", "B", "C"], index=[1, 2])

assert len(frame.index) == 2
assert len(frame.columns) == 3
assert isna(frame).values.all()

# cast type
msg = r"datetime64\[ns\] values and dtype=int64 is not supported"
with pytest.raises(TypeError, match=msg):
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            category=DeprecationWarning,
            message="elementwise comparison failed",
        )
        DataFrame(mat, columns=["A", "B", "C"], index=[1, 2], dtype=np.int64)

        # Check non-masked values
mat2 = ma.copy(mat)
mat2[0, 0] = 1
mat2[1, 2] = 2
frame = DataFrame(mat2, columns=["A", "B", "C"], index=[1, 2])
assert 1 == frame["A"].view("i8")[1]
assert 2 == frame["C"].view("i8")[2]

# masked bool promoted to object
mat = ma.masked_all((2, 3), dtype=bool)
# 2-D input
frame = DataFrame(mat, columns=["A", "B", "C"], index=[1, 2])

assert len(frame.index) == 2
assert len(frame.columns) == 3
assert np.all(~np.asarray(frame == frame))

# cast type
frame = DataFrame(mat, columns=["A", "B", "C"], index=[1, 2], dtype=object)
assert frame.values.dtype == object

# Check non-masked values
mat2 = ma.copy(mat)
mat2[0, 0] = True
mat2[1, 2] = False
frame = DataFrame(mat2, columns=["A", "B", "C"], index=[1, 2])
assert frame["A"][1] is True
assert frame["C"][2] is False
