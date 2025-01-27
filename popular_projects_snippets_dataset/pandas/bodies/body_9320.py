# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_warnings.py
# https://github.com/pandas-dev/pandas/issues/16409
pytest.importorskip("IPython", minversion="6.0.0")
from IPython.core.completer import provisionalcompleter

code = "import pandas as pd; c = Categorical([])"
await ip.run_code(code)

# GH 31324 newer jedi version raises Deprecation warning;
#  appears resolved 2021-02-02
with tm.assert_produces_warning(None):
    with provisionalcompleter("ignore"):
        list(ip.Completer.completions("c.", 1))
