# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
vals = [
    2.08430917305e10,
    3.52205017305e10,
    2.30674817305e10,
    2.03954217305e10,
    5.59897817305e10,
]
for line in repr(Series(vals)).split("\n"):
    if line.startswith("dtype:"):
        continue
    if _three_digit_exp():
        assert "+010" in line
    else:
        assert "+10" in line
