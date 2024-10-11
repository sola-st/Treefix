import pandas as pd # pragma: no cover
from textwrap import dedent # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
_dedent = dedent # pragma: no cover

import pandas as pd # pragma: no cover
from textwrap import dedent # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
_dedent = dedent # pragma: no cover
expected = _dedent(r'''\begin{tabular}{rl}# pragma: no cover
\toprule# pragma: no cover
\midrule# pragma: no cover
1 & b1 \\# pragma: no cover
2 & b2 \\# pragma: no cover
\bottomrule# pragma: no cover
\end{tabular}''' ) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 7124
from l3.Runtime import _l_
df = DataFrame({"a": [1, 2], "b": ["b1", "b2"]})
_l_(10515)
result = df.to_latex(index=False, header=False)
_l_(10516)
expected = _dedent(
    r"""
            \begin{tabular}{rl}
            \toprule
            \midrule
            1 & b1 \\
            2 & b2 \\
            \bottomrule
            \end{tabular}
            """
)
_l_(10517)
assert result == expected
_l_(10518)
