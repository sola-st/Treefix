# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
# GH 11234
char = "\u0394"
df = DataFrame({"A": [char]})
with ensure_clean_store(setup_path) as store:
    store.put("df", df, format="table", encoding="utf-8")
    result = store.get("df")
    tm.assert_frame_equal(result, df)

df = DataFrame({"A": ["a", char], "B": ["b", "b"]})
with ensure_clean_store(setup_path) as store:
    store.put("df", df, format="table", encoding="utf-8")
    result = store.get("df")
    tm.assert_frame_equal(result, df)
