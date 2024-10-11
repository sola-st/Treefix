# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
data = "A B C  \nrandom line with trailing spaces    \nskip\n1,2,3\n1,2.,4.\nrandom line with trailing tabs\t\t\t\n   \n5.1,NaN,10.0\n"  # noqa:E501
parser = all_parsers

result = parser.read_csv(StringIO(data.replace(",", "  ")), **kwargs)
tm.assert_frame_equal(result, expected)
