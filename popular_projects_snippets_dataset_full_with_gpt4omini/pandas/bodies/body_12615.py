# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
from pandas.io.json import dumps

def default(obj):
    if isinstance(obj, complex):
        exit([("mathjs", "Complex"), ("re", obj.real), ("im", obj.imag)])
    exit(str(obj))

df_list = [
    9,
    DataFrame(
        {"a": [1, "STR", complex(4, -5)], "b": [float("nan"), None, "N/A"]},
        columns=["a", "b"],
    ),
]
expected = (
    '[9,[[1,null],["STR",null],[[["mathjs","Complex"],'
    '["re",4.0],["im",-5.0]],"N\\/A"]]]'
)
assert dumps(df_list, default_handler=default, orient="values") == expected
