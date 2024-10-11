# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_invalid.py
# text reader ok
# GH6583
data = """index,A,B,C,D
                  foo,2,3,4,5
                  bar,7,8,9,10
                  baz,12,13,14,15
                  qux,12,13,14,15
                  foo2,12,13,14,15
                  bar2,12,13,14,15
               """

with read_csv(StringIO(data), chunksize=1) as reader:
    result = concat(reader, ignore_index=True)
expected = read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
