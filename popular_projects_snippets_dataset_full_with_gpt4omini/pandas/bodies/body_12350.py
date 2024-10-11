# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 23633
output = [{"mixed": "string" * 500, "number": 0}, {"mixed": None, "number": 1}]
output = DataFrame(output)
output.number = output.number.astype("int32")

with tm.ensure_clean() as path:
    output.to_stata(path, write_index=False, version=117)
    reread = read_stata(path)
    expected = output.fillna("")
    tm.assert_frame_equal(reread, expected)

    # Check strl supports all None (null)
    output["mixed"] = None
    output.to_stata(
        path, write_index=False, convert_strl=["mixed"], version=117
    )
    reread = read_stata(path)
    expected = output.fillna("")
    tm.assert_frame_equal(reread, expected)
