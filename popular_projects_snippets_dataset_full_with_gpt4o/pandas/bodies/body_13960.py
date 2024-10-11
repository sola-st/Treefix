# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
s = Series([1.000000 + 1.000000j, 1.0 + 1.0j, 1.05 + 1.0j])
result = s.to_string()
expected = dedent(
    """\
        0    1.00+1.00j
        1    1.00+1.00j
        2    1.05+1.00j"""
)
assert result == expected
