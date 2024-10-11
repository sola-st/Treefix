from pandas import DataFrame # pragma: no cover
import textwrap # pragma: no cover

def _dedent(text): return textwrap.dedent(text) # pragma: no cover

import pandas as pd # pragma: no cover
from textwrap import dedent # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
expected = dedent("""\n    \\begin{tabular}{rl}\n    \\toprule\n    \\midrule\n    1 & b1 \\  \n    2 & b2 \\  \n    \\bottomrule\n    \\end{tabular}\n    """.strip()) # pragma: no cover

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
