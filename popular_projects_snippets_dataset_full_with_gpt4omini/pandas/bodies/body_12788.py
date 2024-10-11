# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH20030:
result = json_normalize(author_missing_data)
ex_data = [
    {
        "info": np.nan,
        "info.created_at": np.nan,
        "info.last_updated": np.nan,
        "author_name.first": np.nan,
        "author_name.last_name": np.nan,
    },
    {
        "info": None,
        "info.created_at": "11/08/1993",
        "info.last_updated": "26/05/2012",
        "author_name.first": "Jane",
        "author_name.last_name": "Doe",
    },
]
expected = DataFrame(ex_data)
tm.assert_frame_equal(result, expected)
