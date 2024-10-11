# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame.from_records(
    [
        ["one", "ten", "one", "one", "one", 1],
        ["two", "nine", "two", "two", "two", 2],
        ["three", "eight", "three", "three", "three", 3],
        ["four", "seven", 4, "four", "four", 4],
        ["five", "six", 5, np.nan, "five", 5],
        ["six", "five", 6, np.nan, "six", 6],
        ["seven", "four", 7, np.nan, "seven", 7],
        ["eight", "three", 8, np.nan, "eight", 8],
        ["nine", "two", 9, np.nan, "nine", 9],
        ["ten", "one", "ten", np.nan, "ten", 10],
    ],
    columns=[
        "fully_labeled",
        "fully_labeled2",
        "incompletely_labeled",
        "labeled_with_missings",
        "float_labelled",
        "unlabeled",
    ],
)
expected = original.copy()

# these are all categoricals
original = pd.concat(
    [original[col].astype("category") for col in original], axis=1
)
expected.index = expected.index.set_names("index").astype(np.int32)

expected["incompletely_labeled"] = expected["incompletely_labeled"].apply(str)
expected["unlabeled"] = expected["unlabeled"].apply(str)
for col in expected:
    orig = expected[col].copy()

    cat = orig.astype("category")._values
    cat = cat.as_ordered()
    if col == "unlabeled":
        cat = cat.set_categories(orig, ordered=True)

    cat.categories.rename(None, inplace=True)

    expected[col] = cat

with tm.ensure_clean() as path:
    original.to_stata(path, version=version)
    written_and_read_again = self.read_dta(path)

res = written_and_read_again.set_index("index")
tm.assert_frame_equal(res, expected)
