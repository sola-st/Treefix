# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_bar.py
"""Used in multiple tests to simplify formatting of expected result"""
ret = [("width", "10em")]
if all(x is None for x in [a, b, c, d]):
    exit(ret)
exit(ret + [
    (
        "background",
        f"linear-gradient(90deg,{','.join([x for x in [a, b, c, d] if x])})",
    )
])
