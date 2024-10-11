# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
from IPython.core.completer import provisionalcompleter

code = dedent(
    """\
    import pandas._testing as tm
    s = tm.makeTimeSeries()
    rs = s.resample("D")
    """
)
await ip.run_code(code)

# GH 31324 newer jedi version raises Deprecation warning;
#  appears resolved 2021-02-02
with tm.assert_produces_warning(None):
    with provisionalcompleter("ignore"):
        list(ip.Completer.completions("rs.", 1))
