import pandas as pd # pragma: no cover
from textwrap import dedent as _dedent # pragma: no cover

df_with_symbols = pd.DataFrame({'co$e^x$': ['a', 'b'], 'co^l1': ['a', 'b']}) # pragma: no cover

import pandas as pd # pragma: no cover
from textwrap import dedent as _dedent # pragma: no cover

df_with_symbols = pd.DataFrame({'co$e^x$': ['a', 'b'], 'co^l1': ['a', 'b']}) # pragma: no cover
expected = _dedent(r"""# pragma: no cover
        \begin{tabular}{lll}# pragma: no cover
        \toprule# pragma: no cover
         & co\$e\textasciicircum x\$ & co\textasciicircum l1 \\# pragma: no cover
        \midrule# pragma: no cover
        a & a & a \\# pragma: no cover
        b & b & b \\# pragma: no cover
        \bottomrule# pragma: no cover
        \end{tabular}# pragma: no cover
        """) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
from l3.Runtime import _l_
result = df_with_symbols.to_latex()  # default: escape=True
_l_(20566)  # default: escape=True
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
_l_(20567)
assert result == expected
_l_(20568)
