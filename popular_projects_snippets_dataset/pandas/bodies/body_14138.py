# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
with option_context("display.max_rows", 10):
    res = repr(s)
lines = res.split("\n")
lines = [
    line for line in repr(s).split("\n") if not re.match(r"[^\.]*\.+", line)
][:-1]
ncolsizes = len({len(line.strip()) for line in lines})
assert ncolsizes == 1
