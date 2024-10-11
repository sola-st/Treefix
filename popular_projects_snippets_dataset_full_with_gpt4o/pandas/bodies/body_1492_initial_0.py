import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import MultiIndex, DataFrame, to_datetime, Timedelta, Series # pragma: no cover
import pandas._testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# .loc[:,column] setting with slice == len of the column
# GH10408
from l3.Runtime import _l_
levels = [
    ["Region_1"] * 4,
    ["Site_1", "Site_1", "Site_2", "Site_2"],
    [3987227376, 3980680971, 3977723249, 3977723089],
]
_l_(21349)
mi = MultiIndex.from_arrays(levels, names=["Region", "Site", "RespondentID"])
_l_(21350)

clevels = [
    ["Respondent", "Respondent", "Respondent", "OtherCat", "OtherCat"],
    ["Something", "StartDate", "EndDate", "Yes/No", "SomethingElse"],
]
_l_(21351)
cols = MultiIndex.from_arrays(clevels, names=["Level_0", "Level_1"])
_l_(21352)

values = [
    ["A", "5/25/2015 10:59", "5/25/2015 11:22", "Yes", np.nan],
    ["A", "5/21/2015 9:40", "5/21/2015 9:52", "Yes", "Yes"],
    ["A", "5/20/2015 8:27", "5/20/2015 8:41", "Yes", np.nan],
    ["A", "5/20/2015 8:33", "5/20/2015 9:09", "Yes", "No"],
]
_l_(21353)
df = DataFrame(values, index=mi, columns=cols)
_l_(21354)

df.loc[:, ("Respondent", "StartDate")] = to_datetime(
    df.loc[:, ("Respondent", "StartDate")]
)
_l_(21355)
df.loc[:, ("Respondent", "EndDate")] = to_datetime(
    df.loc[:, ("Respondent", "EndDate")]
)
_l_(21356)
df = df.infer_objects(copy=False)
_l_(21357)

# Adding a new key
df.loc[:, ("Respondent", "Duration")] = (
    df.loc[:, ("Respondent", "EndDate")]
    - df.loc[:, ("Respondent", "StartDate")]
)
_l_(21358)

# timedelta64[m] -> float, so this cannot be done inplace, so
#  no warning
df.loc[:, ("Respondent", "Duration")] = df.loc[
    :, ("Respondent", "Duration")
] / Timedelta(60_000_000_000)
_l_(21359)

expected = Series(
    [23.0, 12.0, 14.0, 36.0], index=df.index, name=("Respondent", "Duration")
)
_l_(21360)
tm.assert_series_equal(df[("Respondent", "Duration")], expected)
_l_(21361)
