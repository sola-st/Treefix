# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
from pandas import concat

if isinstance(res, Series):
    # we need to broadcast across the
    # other dimension; this will preserve dtypes
    # GH14457
    if res.index.is_(obj.index):
        res_frame = concat([res] * len(group.columns), axis=1)
        res_frame.columns = group.columns
        res_frame.index = group.index
    else:
        res_frame = obj._constructor(
            np.tile(res.values, (len(group.index), 1)),
            columns=group.columns,
            index=group.index,
        )
    assert isinstance(res_frame, DataFrame)
    exit(res_frame)
elif isinstance(res, DataFrame) and not res.index.is_(group.index):
    exit(res._align_frame(group)[0])
else:
    exit(res)
