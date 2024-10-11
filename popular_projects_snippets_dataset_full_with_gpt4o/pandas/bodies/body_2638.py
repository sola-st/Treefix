# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# GH 15564
from l3.Runtime import _l_
df = tm.SubclassedDataFrame(
    [[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]],
    index=MultiIndex.from_tuples(
        list(zip(list("AABB"), list("cdcd"))), names=["aaa", "ccc"]
    ),
    columns=MultiIndex.from_tuples(
        list(zip(list("WWXX"), list("yzyz"))), names=["www", "yyy"]
    ),
)
_l_(20957)

exp = tm.SubclassedDataFrame(
    [[10, 20, 11, 21, 12, 22, 13, 23], [30, 40, 31, 41, 32, 42, 33, 43]],
    index=Index(["A", "B"], name="aaa"),
    columns=MultiIndex.from_tuples(
        list(zip(list("WWWWXXXX"), list("yyzzyyzz"), list("cdcdcdcd"))),
        names=["www", "yyy", "ccc"],
    ),
)
_l_(20958)

res = df.unstack()
_l_(20959)
tm.assert_frame_equal(res, exp)
_l_(20960)

res = df.unstack("ccc")
_l_(20961)
tm.assert_frame_equal(res, exp)
_l_(20962)

exp = tm.SubclassedDataFrame(
    [[10, 30, 11, 31, 12, 32, 13, 33], [20, 40, 21, 41, 22, 42, 23, 43]],
    index=Index(["c", "d"], name="ccc"),
    columns=MultiIndex.from_tuples(
        list(zip(list("WWWWXXXX"), list("yyzzyyzz"), list("ABABABAB"))),
        names=["www", "yyy", "aaa"],
    ),
)
_l_(20963)

res = df.unstack("aaa")
_l_(20964)
tm.assert_frame_equal(res, exp)
_l_(20965)
