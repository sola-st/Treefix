import pandas as pd # pragma: no cover
from textwrap import dedent # pragma: no cover

_dedent = dedent # pragma: no cover

import pandas as pd # pragma: no cover
from textwrap import dedent # pragma: no cover

data = {0: [0, 1, 0, 5], 1: [0, 1, 5, 6], 2: [2, 3, 6, 7], 3: [3, 4, 7, 8], 4: [4, 9, 8, 9]} # pragma: no cover
multiindex = pd.MultiIndex.from_product([['c1', 'c2', 'c3'], range(2)], names=['index', 'subindex']) # pragma: no cover
_dedent = dedent # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
from l3.Runtime import _l_
result = multicolumn_frame.T.to_latex(multirow=True)
_l_(4528)
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
_l_(4529)
assert result == expected
_l_(4530)
