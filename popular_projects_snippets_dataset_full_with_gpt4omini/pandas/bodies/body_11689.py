# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_converters.py
# see gh-583
converters = {}
parser = all_parsers

data = """Id;Number1;Number2;Text1;Text2;Number3
1;1521,1541;187101,9543;ABC;poi;4,7387
2;121,12;14897,76;DEF;uyt;0,3773
3;878,158;108013,434;GHI;rez;2,7356"""
converters["Number1"] = converters["Number2"] = converters[
    "Number3"
] = lambda x: float(x.replace(",", "."))

result = parser.read_csv(StringIO(data), sep=";", converters=converters)
expected = DataFrame(
    [
        [1, 1521.1541, 187101.9543, "ABC", "poi", 4.7387],
        [2, 121.12, 14897.76, "DEF", "uyt", 0.3773],
        [3, 878.158, 108013.434, "GHI", "rez", 2.7356],
    ],
    columns=["Id", "Number1", "Number2", "Text1", "Text2", "Number3"],
)
tm.assert_frame_equal(result, expected)
