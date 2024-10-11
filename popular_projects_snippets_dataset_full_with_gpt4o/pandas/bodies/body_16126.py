# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# test the tab completion display
ok_for_cat = [
    "categories",
    "codes",
    "ordered",
    "set_categories",
    "add_categories",
    "remove_categories",
    "rename_categories",
    "reorder_categories",
    "remove_unused_categories",
    "as_ordered",
    "as_unordered",
]

s = Series(list("aabbcde")).astype("category")
results = sorted({r for r in s.cat.__dir__() if not r.startswith("_")})
tm.assert_almost_equal(results, sorted(set(ok_for_cat)))
