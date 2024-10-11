import pytest # pragma: no cover
from pandas import option_context, DataFrame # pragma: no cover

import pytest # pragma: no cover
from pandas import option_context, DataFrame # pragma: no cover
from pandas.io.formats.style import Styler # pragma: no cover

Styler.environment = 'latex' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
from l3.Runtime import _l_
pytest.importorskip("jinja2")
_l_(16068)
expected = r"""\begin{tabular}{llll}
\toprule
 & 0 & 1 & 2 \\
\midrule
0 & $\alpha$ & b & c \\
1 & 1 & 2 & 3 \\
\bottomrule
\end{tabular}
"""
_l_(16069)
with option_context(
    "display.latex.escape", False, "styler.render.repr", "latex"
):
    _l_(16073)

    df = DataFrame([[r"$\alpha$", "b", "c"], [1, 2, 3]])
    _l_(16070)
    result = df._repr_latex_()
    _l_(16071)
    assert result == expected
    _l_(16072)

# GH 12182
assert df._repr_latex_() is None
_l_(16074)
