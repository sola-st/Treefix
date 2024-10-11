import pandas as pd # pragma: no cover
from textwrap import dedent as _dedent # pragma: no cover

data = { # pragma: no cover
    'c1': { # pragma: no cover
        0: [0, 1, 2, 3, 4], # pragma: no cover
        1: [5, 6, 7, 8, 9] # pragma: no cover
    }, # pragma: no cover
    'c2': { # pragma: no cover
        0: [0, 1, 2, 3, 4], # pragma: no cover
        1: [5, 6, 7, 8, 9] # pragma: no cover
    }, # pragma: no cover
    'c3': { # pragma: no cover
        0: [0, 1, 2, 3, 4] # pragma: no cover
    } # pragma: no cover
} # pragma: no cover
multicolumn_frame = pd.DataFrame( # pragma: no cover
    [(k1, k2, *v) for k1, d in data.items() for k2, v in d.items()], # pragma: no cover
    columns=['col1', 'col2', 0, 1, 2, 3, 4] # pragma: no cover
).set_index(['col1', 'col2']).stack().unstack(level=[0, 1]) # pragma: no cover
def _l_(x): pass # pragma: no cover

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
