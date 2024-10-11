import pandas as pd # pragma: no cover
from textwrap import dedent as _dedent # pragma: no cover
from unittest.mock import MagicMock as _l_ # pragma: no cover

df_with_symbols = pd.DataFrame({'co\$e\textasciicircum x\$': ['a', 'b'], 'co\textasciicircum l1': ['a', 'b']}) # pragma: no cover
_l_ = type('Mock', (object,), {'__call__': lambda self, x: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
from l3.Runtime import _l_
result = df_with_symbols.to_latex()  # default: escape=True
_l_(9747)  # default: escape=True
expected = _dedent(
    r"""
            \begin{tabular}{lll}
            \toprule
             & co\$e\textasciicircum x\$ & co\textasciicircum l1 \\
            \midrule
            a & a & a \\
            b & b & b \\
            \bottomrule
            \end{tabular}
            """
)
_l_(9748)
assert result == expected
_l_(9749)
