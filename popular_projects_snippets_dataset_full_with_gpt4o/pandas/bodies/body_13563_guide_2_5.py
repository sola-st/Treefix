import pandas as pd # pragma: no cover
from textwrap import dedent as _dedent # pragma: no cover

data = { # pragma: no cover
    'c1_0': [0, 5], # pragma: no cover
    'c1_1': [1, 6], # pragma: no cover
    'c1_2': [2, 7], # pragma: no cover
    'c1_3': [3, 8], # pragma: no cover
    'c1_4': [4, 9], # pragma: no cover
    'c2_0': [0, 5], # pragma: no cover
    'c2_1': [1, 6], # pragma: no cover
    'c2_2': [2, 7], # pragma: no cover
    'c2_3': [3, 8], # pragma: no cover
    'c2_4': [4, 9], # pragma: no cover
    'c3_0': [0, 0], # pragma: no cover
    'c3_1': [1, 1], # pragma: no cover
    'c3_2': [2, 2], # pragma: no cover
    'c3_3': [3, 3], # pragma: no cover
    'c3_4': [4, 4] # pragma: no cover
} # pragma: no cover
multicolumn_frame = pd.DataFrame(data) # pragma: no cover
multicolumn_frame.columns = pd.MultiIndex.from_tuples([('c1', 0), ('c1', 1), ('c1', 2), ('c1', 3), ('c1', 4), # pragma: no cover
                                                       ('c2', 0), ('c2', 1), ('c2', 2), ('c2', 3), ('c2', 4), # pragma: no cover
                                                       ('c3', 0), ('c3', 1), ('c3', 2), ('c3', 3), ('c3', 4)]) # pragma: no cover
multicolumn_frame = multicolumn_frame.T # pragma: no cover
def _l_(x): # pragma: no cover
    pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
from l3.Runtime import _l_
result = multicolumn_frame.T.to_latex(multirow=True)
_l_(16075)
expected = _dedent(
    r"""
            \begin{tabular}{llrrrrr}
            \toprule
             &  & 0 & 1 & 2 & 3 & 4 \\
            \midrule
            \multirow[t]{2}{*}{c1} & 0 & 0 & 1 & 2 & 3 & 4 \\
             & 1 & 5 & 6 & 7 & 8 & 9 \\
            \cline{1-7}
            \multirow[t]{2}{*}{c2} & 0 & 0 & 1 & 2 & 3 & 4 \\
             & 1 & 5 & 6 & 7 & 8 & 9 \\
            \cline{1-7}
            c3 & 0 & 0 & 1 & 2 & 3 & 4 \\
            \cline{1-7}
            \bottomrule
            \end{tabular}
            """
)
_l_(16076)
assert result == expected
_l_(16077)
