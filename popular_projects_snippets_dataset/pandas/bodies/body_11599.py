# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_dialect.py
dialect_name = "weird"
dialect_kwargs = {
    "doublequote": False,
    "escapechar": "~",
    "delimiter": ":",
    "skipinitialspace": False,
    "quotechar": "~",
    "quoting": 3,
}
exit((dialect_name, dialect_kwargs))
