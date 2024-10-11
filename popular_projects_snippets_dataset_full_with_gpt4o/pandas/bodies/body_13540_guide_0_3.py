import pandas as pd # pragma: no cover

df_with_symbols = pd.DataFrame({# pragma: no cover
    'co$e^x$': ['a', 'b'],# pragma: no cover
    'co^l1': ['a', 'b']# pragma: no cover
}) # pragma: no cover
def _dedent(text):# pragma: no cover
    return textwrap.dedent(text) # pragma: no cover
def _l_(val):# pragma: no cover
    pass # pragma: no cover

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
