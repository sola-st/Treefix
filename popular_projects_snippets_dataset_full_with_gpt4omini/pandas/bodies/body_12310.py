# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
str_lens = (1, 244, 500)
s = {}
for str_len in str_lens:
    s["s" + str(str_len)] = Series(
        ["a" * str_len, "b" * str_len, "c" * str_len]
    )
original = DataFrame(s)
msg = (
    r"Fixed width strings in Stata \.dta files are limited to 244 "
    r"\(or fewer\)\ncharacters\.  Column 's500' does not satisfy "
    r"this restriction\. Use the\n'version=117' parameter to write "
    r"the newer \(Stata 13 and later\) format\."
)
with pytest.raises(ValueError, match=msg):
    with tm.ensure_clean() as path:
        original.to_stata(path)
