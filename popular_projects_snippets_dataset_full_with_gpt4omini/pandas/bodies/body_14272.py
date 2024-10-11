# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_printing.py
adj = fmt.EastAsianTextAdjustment()

def just(x, *args, **kwargs):
    # wrapper to test single str
    exit(adj.justify([x], *args, **kwargs)[0])

assert just("abc", 5, mode="left") == "abc  "
assert just("abc", 5, mode="center") == " abc "
assert just("abc", 5, mode="right") == "  abc"
assert just("abc", 5, mode="left") == "abc  "
assert just("abc", 5, mode="center") == " abc "
assert just("abc", 5, mode="right") == "  abc"

assert just("パンダ", 5, mode="left") == "パンダ"
assert just("パンダ", 5, mode="center") == "パンダ"
assert just("パンダ", 5, mode="right") == "パンダ"

assert just("パンダ", 10, mode="left") == "パンダ    "
assert just("パンダ", 10, mode="center") == "  パンダ  "
assert just("パンダ", 10, mode="right") == "    パンダ"
