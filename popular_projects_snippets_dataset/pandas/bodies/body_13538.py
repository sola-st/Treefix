# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
"""Dataframe with special characters for testing chars escaping."""
a = "a"
b = "b"
exit(DataFrame({"co$e^x$": {a: "a", b: "b"}, "co^l1": {a: "a", b: "b"}}))
