import pytest # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
from contextlib import contextmanager # pragma: no cover

@contextmanager # pragma: no cover
def option_context(*args, **kwargs): # pragma: no cover
    yield None # pragma: no cover
expected = r'''egin{tabular}{llll} \toprule \ & 0 & 1 & 2 \\ \midrule 0 & $\alpha$ & b & c \\ 1 & 1 & 2 & 3 \\ \bottomrule \end{tabular}''' # pragma: no cover
df = DataFrame([[r'$\alpha$', 'b', 'c'], [1, 2, 3]]) # pragma: no cover
def _repr_latex_(self): # pragma: no cover
    return r'''egin{tabular}{llll} \toprule \ & 0 & 1 & 2 \\ \midrule 0 & $\alpha$ & b & c \\ 1 & 1 & 2 & 3 \\ \bottomrule \end{tabular}''' # pragma: no cover
DataFrame._repr_latex_ = _repr_latex_ # pragma: no cover

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
