# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
data = [
    "dave@google.com",
    "tdhock5@gmail.com",
    "maudelaperriere@gmail.com",
    "rob@gmail.com some text steve@gmail.com",
    "a@b.com some text c@d.com and e@f.com",
    np.nan,
    "",
]
expected_tuples = [
    ("dave", "google", "com"),
    ("tdhock5", "gmail", "com"),
    ("maudelaperriere", "gmail", "com"),
    ("rob", "gmail", "com"),
    ("steve", "gmail", "com"),
    ("a", "b", "com"),
    ("c", "d", "com"),
    ("e", "f", "com"),
]
pat = r"""
    (?P<user>[a-z0-9]+)
    @
    (?P<domain>[a-z]+)
    \.
    (?P<tld>[a-z]{2,4})
    """
expected_columns = ["user", "domain", "tld"]
s = Series(data, dtype=any_string_dtype)
# extractall should return a DataFrame with one row for each match, indexed by the
# subject from which the match came.
expected_index = MultiIndex.from_tuples(
    [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 0), (4, 1), (4, 2)],
    names=(None, "match"),
)
expected = DataFrame(
    expected_tuples, expected_index, expected_columns, dtype=any_string_dtype
)
result = s.str.extractall(pat, flags=re.VERBOSE)
tm.assert_frame_equal(result, expected)

# The index of the input Series should be used to construct the index of the output
# DataFrame:
mi = MultiIndex.from_tuples(
    [
        ("single", "Dave"),
        ("single", "Toby"),
        ("single", "Maude"),
        ("multiple", "robAndSteve"),
        ("multiple", "abcdef"),
        ("none", "missing"),
        ("none", "empty"),
    ]
)
s = Series(data, index=mi, dtype=any_string_dtype)
expected_index = MultiIndex.from_tuples(
    [
        ("single", "Dave", 0),
        ("single", "Toby", 0),
        ("single", "Maude", 0),
        ("multiple", "robAndSteve", 0),
        ("multiple", "robAndSteve", 1),
        ("multiple", "abcdef", 0),
        ("multiple", "abcdef", 1),
        ("multiple", "abcdef", 2),
    ],
    names=(None, None, "match"),
)
expected = DataFrame(
    expected_tuples, expected_index, expected_columns, dtype=any_string_dtype
)
result = s.str.extractall(pat, flags=re.VERBOSE)
tm.assert_frame_equal(result, expected)

# MultiIndexed subject with names.
s = Series(data, index=mi, dtype=any_string_dtype)
s.index.names = ("matches", "description")
expected_index.names = ("matches", "description", "match")
expected = DataFrame(
    expected_tuples, expected_index, expected_columns, dtype=any_string_dtype
)
result = s.str.extractall(pat, flags=re.VERBOSE)
tm.assert_frame_equal(result, expected)
