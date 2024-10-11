import pandas as pd # pragma: no cover
import pytest # pragma: no cover

df_duplabels = pd.DataFrame({('L1', 'L2', 'L3'): [1, 2, 3], ('L1', 'L2', 'L4'): [4, 5, 6]}) # pragma: no cover
axis = 0 # pragma: no cover
def assert_level_values(df, levels, axis): assert all(level in df.axes[axis].names for level in levels) # pragma: no cover
def assert_label_values(df, labels, axis): unique_labels = df.axes[axis]; assert all(label in unique_labels for label in labels); assert len(set(unique_labels)) == len(unique_labels) # pragma: no cover
df_duplabels._get_axis_number = lambda axis: axis # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py

from l3.Runtime import _l_
axis = df_duplabels._get_axis_number(axis)
_l_(22354)
# Transpose frame if axis == 1
if axis == 1:
    _l_(22356)

    df_duplabels = df_duplabels.T
    _l_(22355)

# df has unambiguous level 'L1'
assert_level_values(df_duplabels, ["L1"], axis=axis)
_l_(22357)

# df has unique label 'L3'
assert_label_values(df_duplabels, ["L3"], axis=axis)
_l_(22358)

# df has duplicate labels 'L2'
if axis == 0:
    _l_(22361)

    expected_msg = "The column label 'L2' is not unique"
    _l_(22359)
else:
    expected_msg = "The index label 'L2' is not unique"
    _l_(22360)

with pytest.raises(ValueError, match=expected_msg):
    _l_(22363)

    assert_label_values(df_duplabels, ["L2"], axis=axis)
    _l_(22362)
