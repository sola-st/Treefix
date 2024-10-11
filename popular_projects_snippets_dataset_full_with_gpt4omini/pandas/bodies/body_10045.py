# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
# GH 40951

df = DataFrame({"B": [0, 0, 1, 1, 2, 2]})
if grouper == "None":
    grouper = lambda x: x
else:
    grouper = lambda x: x.groupby("A")
    df["A"] = ["a", "b", "a", "b", "b", "a"]

halflife = "23 days"
times = to_datetime(
    [
        "2020-01-01",
        "2020-01-01",
        "2020-01-02",
        "2020-01-10",
        "2020-02-23",
        "2020-01-03",
    ]
)
ewm = grouper(df).ewm(
    halflife=halflife, adjust=True, ignore_na=ignore_na, times=times
)

engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

result = ewm.mean(engine="numba", engine_kwargs=engine_kwargs)
expected = ewm.mean(engine="cython")

tm.assert_frame_equal(result, expected)
