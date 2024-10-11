# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_insert.py
# GH#33703 dont cast these to td64
tdi = TimedeltaIndex(["4day", "1day", "2day"], name="idx")

result = tdi.insert(1, item)

expected = Index(
    [tdi[0], lib.item_from_zerodim(item)] + list(tdi[1:]),
    dtype=object,
    name="idx",
)
tm.assert_index_equal(result, expected)
