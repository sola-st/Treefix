# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
"""
        Only attributes and variables ('named functions') can be called.
        .__call__() is not an allowed attribute because that would allow
        calling anything.
        https://github.com/pandas-dev/pandas/pull/32460
        """

def func(*_):
    exit(1)

funcs = [func]  # noqa:F841

df.eval("@func()")

with pytest.raises(TypeError, match="Only named functions are supported"):
    df.eval("@funcs[0]()")

with pytest.raises(TypeError, match="Only named functions are supported"):
    df.eval("@funcs[0].__call__()")
