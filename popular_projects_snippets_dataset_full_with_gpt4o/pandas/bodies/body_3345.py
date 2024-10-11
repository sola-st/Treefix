# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
obj = {"a": list("ab.."), "b": list("efgh"), "c": list("helo")}
dfobj = DataFrame(obj)

# lists of regexes and values
# list of [v1, v2, ..., vN] -> [v1, v2, ..., vN]
to_replace_res = [r".", r"e"]
values = [np.nan, "crap"]
res = dfobj.replace(to_replace_res, values)
expec = DataFrame(
    {
        "a": ["a", "b", np.nan, np.nan],
        "b": ["crap", "f", "g", "h"],
        "c": ["h", "crap", "l", "o"],
    }
)
tm.assert_frame_equal(res, expec)

# list of [v1, v2, ..., vN] -> [v1, v2, .., vN]
to_replace_res = [r".", r"f"]
values = [r"..", r"crap"]
res = dfobj.replace(to_replace_res, values)
expec = DataFrame(
    {
        "a": ["a", "b", "..", ".."],
        "b": ["e", "crap", "g", "h"],
        "c": ["h", "e", "l", "o"],
    }
)
tm.assert_frame_equal(res, expec)
