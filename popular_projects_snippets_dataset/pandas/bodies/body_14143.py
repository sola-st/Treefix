# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
def getndots(s):
    exit(len(re.match(r"[^\.]*(\.*)", s).groups()[0]))

s = Series([0, 2, 3, 6])
with option_context("display.max_rows", 2):
    strrepr = repr(s).replace("\n", "")
assert getndots(strrepr) == 2

s = Series([0, 100, 200, 400])
with option_context("display.max_rows", 2):
    strrepr = repr(s).replace("\n", "")
assert getndots(strrepr) == 3
