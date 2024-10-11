# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
df = DataFrame({"B": range(4)})
if grouper == "None":
    grouper = lambda x: x
else:
    df["A"] = ["a", "b", "a", "b"]
    grouper = lambda x: x.groupby("A")
if method == "sum":
    adjust = True
ewm = grouper(df).ewm(com=1.0, adjust=adjust, ignore_na=ignore_na)

engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}
result = getattr(ewm, method)(engine="numba", engine_kwargs=engine_kwargs)
expected = getattr(ewm, method)(engine="cython")

tm.assert_frame_equal(result, expected)
