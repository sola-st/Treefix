import pandas as pd # pragma: no cover
import pytest # pragma: no cover

df_duplabels = pd.DataFrame({'L1': [1, 2], 'L2': [1, 1], 'L3': [3, 4]}).set_index('L1') # pragma: no cover
axis = 0 # pragma: no cover
def assert_level_values(df, levels, axis): pass # pragma: no cover
def assert_label_values(df, labels, axis): pass # pragma: no cover
df_duplabels._get_axis_number = lambda x: (0 if x == 'index' else 1) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py

from l3.Runtime import _l_
axis = df_duplabels._get_axis_number(axis)
_l_(10778)
# Transpose frame if axis == 1
if axis == 1:
    _l_(10780)

    df_duplabels = df_duplabels.T
    _l_(10779)

# df has unambiguous level 'L1'
assert_level_values(df_duplabels, ["L1"], axis=axis)
_l_(10781)

# df has unique label 'L3'
assert_label_values(df_duplabels, ["L3"], axis=axis)
_l_(10782)

# df has duplicate labels 'L2'
if axis == 0:
    _l_(10785)

    expected_msg = "The column label 'L2' is not unique"
    _l_(10783)
else:
    expected_msg = "The index label 'L2' is not unique"
    _l_(10784)

with pytest.raises(ValueError, match=expected_msg):
    _l_(10787)

    assert_label_values(df_duplabels, ["L2"], axis=axis)
    _l_(10786)
