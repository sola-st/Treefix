# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# GH 15564
df = tm.SubclassedDataFrame(
    [[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]],
    index=MultiIndex.from_tuples(
        list(zip(list("AABB"), list("cdcd"))), names=["aaa", "ccc"]
    ),
    columns=MultiIndex.from_tuples(
        list(zip(list("WWXX"), list("yzyz"))), names=["www", "yyy"]
    ),
)

exp = tm.SubclassedDataFrame(
    [
        [10, 12],
        [11, 13],
        [20, 22],
        [21, 23],
        [30, 32],
        [31, 33],
        [40, 42],
        [41, 43],
    ],
    index=MultiIndex.from_tuples(
        list(zip(list("AAAABBBB"), list("ccddccdd"), list("yzyzyzyz"))),
        names=["aaa", "ccc", "yyy"],
    ),
    columns=Index(["W", "X"], name="www"),
)

res = df.stack()
tm.assert_frame_equal(res, exp)

res = df.stack("yyy")
tm.assert_frame_equal(res, exp)

exp = tm.SubclassedDataFrame(
    [
        [10, 11],
        [12, 13],
        [20, 21],
        [22, 23],
        [30, 31],
        [32, 33],
        [40, 41],
        [42, 43],
    ],
    index=MultiIndex.from_tuples(
        list(zip(list("AAAABBBB"), list("ccddccdd"), list("WXWXWXWX"))),
        names=["aaa", "ccc", "www"],
    ),
    columns=Index(["y", "z"], name="yyy"),
)

res = df.stack("www")
tm.assert_frame_equal(res, exp)
