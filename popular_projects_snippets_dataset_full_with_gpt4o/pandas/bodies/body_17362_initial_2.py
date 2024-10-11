import pandas as pd # pragma: no cover
import pytest # pragma: no cover

df_duplabels = pd.DataFrame({'L1': [1, 2], 'L2': [3, 4], 'L2': [5, 6]}, index=['L3', 'L3']) # pragma: no cover
axis = 0 # pragma: no cover
def assert_level_values(df, levels, axis): assert_index_equal(df.columns if axis == 0 else df.index, pd.Index(levels)) # pragma: no cover
def assert_label_values(df, labels, axis): assert labels[0] not in df.columns if axis == 0 else labels[0] not in df.index # pragma: no cover
pytest = type('Mock', (object,), {'raises': pytest.raises}) # pragma: no cover
df_duplabels._get_axis_number = lambda axis: {'index': 0, 'columns': 1}.get(axis, axis) # pragma: no cover

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
