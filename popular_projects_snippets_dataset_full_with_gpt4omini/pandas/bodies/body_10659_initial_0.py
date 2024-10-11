import pandas as pd # pragma: no cover

tm = type('Mock', (object,), {'assert_frame_equal': lambda self, df1, df2: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply_mutate.py
# GH#44803
from l3.Runtime import _l_
df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Carl"],
        "age": [20, 21, 20],
    }
).set_index("name")
_l_(10114)

grp_by_same_value = df.groupby(["age"], group_keys=False).apply(lambda group: group)
_l_(10115)
grp_by_copy = df.groupby(["age"], group_keys=False).apply(
    lambda group: group.copy()
)
_l_(10116)
tm.assert_frame_equal(grp_by_same_value, grp_by_copy)
_l_(10117)
