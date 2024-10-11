# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# gh-7626 - Read only nrows of data in for large inputs (>262144b)
parser = c_parser_only
header_narrow = "\t".join(["COL_HEADER_" + str(i) for i in range(10)]) + "\n"
data_narrow = "\t".join(["somedatasomedatasomedata1" for _ in range(10)]) + "\n"
header_wide = "\t".join(["COL_HEADER_" + str(i) for i in range(15)]) + "\n"
data_wide = "\t".join(["somedatasomedatasomedata2" for _ in range(15)]) + "\n"
test_input = header_narrow + data_narrow * 1050 + header_wide + data_wide * 2

df = parser.read_csv(StringIO(test_input), sep="\t", nrows=1010)

assert df.size == 1010 * 10
