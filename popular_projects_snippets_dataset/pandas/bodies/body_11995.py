# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
data = """index1,index2,A,B,C
20090101,one,a,1,2
20090101,two,b,3,4
20090101,three,c,4,5
20090102,one,a,1,2
20090102,two,b,3,4
20090102,three,c,4,5
20090103,one,a,1,2
20090103,two,b,3,4
20090103,three,c,4,5
"""
parser = all_parsers
index = MultiIndex.from_product(
    [
        (datetime(2009, 1, 1), datetime(2009, 1, 2), datetime(2009, 1, 3)),
        ("one", "two", "three"),
    ],
    names=["index1", "index2"],
)

# Out of order.
if index_col == [1, 0]:
    index = index.swaplevel(0, 1)

expected = DataFrame(
    [
        ["a", 1, 2],
        ["b", 3, 4],
        ["c", 4, 5],
        ["a", 1, 2],
        ["b", 3, 4],
        ["c", 4, 5],
        ["a", 1, 2],
        ["b", 3, 4],
        ["c", 4, 5],
    ],
    columns=["A", "B", "C"],
    index=index,
)
result = parser.read_csv_check_warnings(
    UserWarning,
    "Could not infer format",
    StringIO(data),
    index_col=index_col,
    parse_dates=True,
)
tm.assert_frame_equal(result, expected)
