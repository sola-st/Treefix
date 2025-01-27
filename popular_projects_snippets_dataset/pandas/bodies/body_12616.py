# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH12554 to_json raises 'Unhandled numpy dtype 15'
df = DataFrame(
    {"a": [1, 2.3, complex(4, -5)], "b": [float("nan"), None, complex(1.2, 0)]},
    columns=["a", "b"],
)
expected = (
    '[["(1+0j)","(nan+0j)"],'
    '["(2.3+0j)","(nan+0j)"],'
    '["(4-5j)","(1.2+0j)"]]'
)
assert df.to_json(default_handler=str, orient="values") == expected
