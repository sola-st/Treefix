# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
# GH 16409
pytest.importorskip("IPython", minversion="6.0.0")
from IPython.core.completer import provisionalcompleter

if frame_or_series is DataFrame:
    code = "from pandas import DataFrame; obj = DataFrame()"
else:
    code = "from pandas import Series; obj = Series(dtype=object)"

await ip.run_code(code)

# GH 31324 newer jedi version raises Deprecation warning;
#  appears resolved 2021-02-02
with tm.assert_produces_warning(None):
    with provisionalcompleter("ignore"):
        list(ip.Completer.completions("obj.", 1))
