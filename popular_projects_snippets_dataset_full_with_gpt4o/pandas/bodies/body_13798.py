# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
df = DataFrame({"A": [1, 0]})
s = df.style
s.ctx = {(0, 0): [("color", "red")], (1, 0): [("", "")]}

result = s._translate(True, True)["cellstyle"]
expected = [
    {"props": [("color", "red")], "selectors": ["row0_col0"]},
    {"props": [("", "")], "selectors": ["row1_col0"]},
]
assert result == expected
