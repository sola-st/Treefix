# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_string.py
df = styler.data
styler1 = styler
styler2 = Styler(df.agg(["sum"]), uuid_len=0, precision=3)
styler3 = Styler(df.agg(["sum"]), uuid_len=0, precision=4)
result = styler1.concat(styler2).concat(styler3).to_string()
expected = dedent(
    """\
     A B C
    0 0 -0.61 ab
    1 1 -1.22 cd
    sum 1 -1.830 abcd
    sum 1 -1.8300 abcd
    """
)
assert result == expected
