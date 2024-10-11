import pandas as pd # pragma: no cover
from pandas import MultiIndex, Index # pragma: no cover

class Mock: pass # pragma: no cover
tm = Mock() # pragma: no cover
tm.SubclassedDataFrame = pd.DataFrame # pragma: no cover
tm.assert_frame_equal = pd.testing.assert_frame_equal # pragma: no cover
MultiIndex = pd.MultiIndex # pragma: no cover
Index = pd.Index # pragma: no cover

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
_l_(9904)

exp = tm.SubclassedDataFrame(
    [[10, 20, 11, 21, 12, 22, 13, 23], [30, 40, 31, 41, 32, 42, 33, 43]],
    index=Index(["A", "B"], name="aaa"),
    columns=MultiIndex.from_tuples(
        list(zip(list("WWWWXXXX"), list("yyzzyyzz"), list("cdcdcdcd"))),
        names=["www", "yyy", "ccc"],
    ),
)
_l_(9905)

res = df.unstack()
_l_(9906)
tm.assert_frame_equal(res, exp)
_l_(9907)

res = df.unstack("ccc")
_l_(9908)
tm.assert_frame_equal(res, exp)
_l_(9909)

exp = tm.SubclassedDataFrame(
    [[10, 30, 11, 31, 12, 32, 13, 33], [20, 40, 21, 41, 22, 42, 23, 43]],
    index=Index(["c", "d"], name="ccc"),
    columns=MultiIndex.from_tuples(
        list(zip(list("WWWWXXXX"), list("yyzzyyzz"), list("ABABABAB"))),
        names=["www", "yyy", "aaa"],
    ),
)
_l_(9910)

res = df.unstack("aaa")
_l_(9911)
tm.assert_frame_equal(res, exp)
_l_(9912)
