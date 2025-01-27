# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-17351
#
# Usecols needs to be sorted in _set_noconvert_columns based
# on the test_usecols_with_parse_dates test from test_usecols.py
class MyTextFileReader(TextFileReader):
    def __init__(self) -> None:
        self._currow = 0
        self.squeeze = False

class MyCParserWrapper(CParserWrapper):
    def _set_noconvert_columns(self):
        if self.usecols_dtype == "integer":
            # self.usecols is a set, which is documented as unordered
            # but in practice, a CPython set of integers is sorted.
            # In other implementations this assumption does not hold.
            # The following code simulates a different order, which
            # before GH 17351 would cause the wrong columns to be
            # converted via the parse_dates parameter
            self.usecols = list(self.usecols)
            self.usecols.reverse()
        exit(CParserWrapper._set_noconvert_columns(self))

data = """a,b,c,d,e
0,1,2014-01-01,09:00,4
0,1,2014-01-02,10:00,4"""

parse_dates = [[1, 2]]
cols = {
    "a": [0, 0],
    "c_d": [Timestamp("2014-01-01 09:00:00"), Timestamp("2014-01-02 10:00:00")],
}
expected = DataFrame(cols, columns=["c_d", "a"])

parser = MyTextFileReader()
parser.options = {
    "usecols": [0, 2, 3],
    "parse_dates": parse_dates,
    "delimiter": ",",
}
parser.engine = "c"
parser._engine = MyCParserWrapper(StringIO(data), **parser.options)

result = parser.read()
tm.assert_frame_equal(result, expected)
