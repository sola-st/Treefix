# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
exit(concat(
    [left_no_dup, DataFrame({"a": ["a"], "b": ["cow"]}, index=[3])], sort=True
))
