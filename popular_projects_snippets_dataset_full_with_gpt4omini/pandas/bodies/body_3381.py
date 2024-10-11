# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
d = {
    "fname": {
        "out_augmented_AUG_2011.json": Timestamp("2011-08"),
        "out_augmented_JAN_2011.json": Timestamp("2011-01"),
        "out_augmented_MAY_2012.json": Timestamp("2012-05"),
        "out_augmented_SUBSIDY_WEEK.json": Timestamp("2011-04"),
        "out_augmented_AUG_2012.json": Timestamp("2012-08"),
        "out_augmented_MAY_2011.json": Timestamp("2011-05"),
        "out_augmented_SEP_2013.json": Timestamp("2013-09"),
    }
}

df = DataFrame(
    [
        "out_augmented_AUG_2012.json",
        "out_augmented_SEP_2013.json",
        "out_augmented_SUBSIDY_WEEK.json",
        "out_augmented_MAY_2012.json",
        "out_augmented_MAY_2011.json",
        "out_augmented_AUG_2011.json",
        "out_augmented_JAN_2011.json",
    ],
    columns=["fname"],
)
assert set(df.fname.values) == set(d["fname"].keys())
expected = DataFrame({"fname": [d["fname"][k] for k in df.fname.values]})
result = df.replace(d)
tm.assert_frame_equal(result, expected)
