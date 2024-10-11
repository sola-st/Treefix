# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-26545
parser = all_parsers
data = '''\ufeff"Head1"\t"Head2"\t"Head3"'''

result = parser.read_csv(StringIO(data), delimiter="\t")
expected = DataFrame(columns=["Head1", "Head2", "Head3"])
tm.assert_frame_equal(result, expected)
