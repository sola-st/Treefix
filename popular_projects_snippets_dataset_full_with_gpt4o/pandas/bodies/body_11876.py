# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
# File with missing values.
test = """index                             A    B    C
2000-01-03T00:00:00  0.980268513777    3  foo
2000-01-04T00:00:00  1.04791624281    -4  bar
                     0.498580885705   73  baz
2000-01-06T00:00:00  1.12020151869     1  foo
2000-01-07T00:00:00                    0  bar
2000-01-10T00:00:00  0.836648671666    2  baz
                                      34"""
colspecs = ((0, 19), (21, 35), (38, 40), (42, 45))
expected = read_fwf(StringIO(test), colspecs=colspecs)

result = read_fwf(StringIO(test))
tm.assert_frame_equal(result, expected)
