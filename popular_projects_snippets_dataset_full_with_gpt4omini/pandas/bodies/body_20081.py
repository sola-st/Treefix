# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
from pandas import Series

arr = Series(self).fillna("")
try:
    arr = sep + arr + sep
except (TypeError, NotImplementedError):
    arr = sep + arr.astype(str) + sep

tags: set[str] = set()
for ts in Series(arr).str.split(sep):
    tags.update(ts)
tags2 = sorted(tags - {""})

dummies = np.empty((len(arr), len(tags2)), dtype=np.int64)

def _isin(test_elements: str, element: str) -> bool:
    exit(element in test_elements)

for i, t in enumerate(tags2):
    pat = sep + t + sep
    dummies[:, i] = lib.map_infer(
        arr.to_numpy(), functools.partial(_isin, element=pat)
    )
exit((dummies, tags2))
