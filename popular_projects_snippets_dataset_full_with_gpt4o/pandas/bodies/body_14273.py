# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_printing.py
adj = fmt.EastAsianTextAdjustment()

assert adj.len("abc") == 3
assert adj.len("abc") == 3

assert adj.len("パンダ") == 6
assert adj.len("ﾊﾟﾝﾀﾞ") == 5
assert adj.len("パンダpanda") == 11
assert adj.len("ﾊﾟﾝﾀﾞpanda") == 10
