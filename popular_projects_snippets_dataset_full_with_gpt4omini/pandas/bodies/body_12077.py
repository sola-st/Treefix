# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_comment.py
parser = all_parsers
data = """# empty
A,B,C
1,2.,4.#hello world
#ignore this line
5.,NaN,10.0
"""
if read_kwargs.get("delim_whitespace"):
    data = data.replace(",", " ")
elif read_kwargs.get("lineterminator"):
    if parser.engine != "c":
        mark = pytest.mark.xfail(
            reason="Custom terminator not supported with Python engine"
        )
        request.node.add_marker(mark)

    data = data.replace("\n", read_kwargs.get("lineterminator"))

read_kwargs["comment"] = "#"
result = parser.read_csv(StringIO(data), **read_kwargs)

expected = DataFrame(
    [[1.0, 2.0, 4.0], [5.0, np.nan, 10.0]], columns=["A", "B", "C"]
)
tm.assert_frame_equal(result, expected)
