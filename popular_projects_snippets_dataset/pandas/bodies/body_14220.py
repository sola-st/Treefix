# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
a = "str<ing1 &amp;"
b = "stri>ng2 &amp;"

test_dict = {"co<l1": {a: string, b: string}, "co>l2": {a: string, b: string}}
result = DataFrame(test_dict).to_html(**kwargs)
expected = expected_html(datapath, expected)
assert result == expected
