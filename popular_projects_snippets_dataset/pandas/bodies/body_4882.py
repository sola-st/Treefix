# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# GH 15055
values = Series(["fooBAD__barBAD", np.nan], dtype=any_string_dtype)

# test with wrong number of arguments, raising an error
msg = (
    r"((takes)|(missing)) (?(2)from \d+ to )?\d+ "
    r"(?(3)required )positional arguments?"
)
with pytest.raises(TypeError, match=msg):
    with tm.maybe_produces_warning(
        PerformanceWarning, any_string_dtype == "string[pyarrow]"
    ):
        values.str.replace("a", repl, regex=True)
