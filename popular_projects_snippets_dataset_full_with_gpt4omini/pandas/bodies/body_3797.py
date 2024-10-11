# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
exit(concat(
    [right_no_dup, DataFrame({"a": ["e"], "c": ["moo"]}, index=[3])]
).set_index("a"))
