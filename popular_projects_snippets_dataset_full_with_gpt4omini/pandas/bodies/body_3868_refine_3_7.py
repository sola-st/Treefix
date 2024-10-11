import pytest # pragma: no cover
from pandas import DataFrame # pragma: no cover
from pandas import option_context # pragma: no cover

DataFrame = type('MockDataFrame', (object,), {'_repr_latex_': lambda self: expected}) # pragma: no cover
option_context = type('MockOptionContext', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_val, exc_tb: None})() # pragma: no cover

import pytest # pragma: no cover
from pandas import DataFrame # pragma: no cover
from contextlib import contextmanager # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
from l3.Runtime import _l_
pytest.importorskip("jinja2")
_l_(4872)
expected = r"""\begin{tabular}{llll}
\toprule
 & 0 & 1 & 2 \\
\midrule
0 & $\alpha$ & b & c \\
1 & 1 & 2 & 3 \\
\bottomrule
\end{tabular}
"""
_l_(4873)
with option_context(
    "display.latex.escape", False, "styler.render.repr", "latex"
):
    _l_(4877)

    df = DataFrame([[r"$\alpha$", "b", "c"], [1, 2, 3]])
    _l_(4874)
    result = df._repr_latex_()
    _l_(4875)
    assert result == expected
    _l_(4876)

# GH 12182
assert df._repr_latex_() is None
_l_(4878)
