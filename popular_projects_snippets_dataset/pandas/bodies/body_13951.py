# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
n = "\u05d0".encode()

with option_context("display.max_rows", 1):
    df = DataFrame([1, 2], columns=[n])
    repr(df)
