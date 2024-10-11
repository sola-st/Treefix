# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH8645 check concat works with tuples, list, generators, and weird
# stuff like deque and custom iterables
df1 = DataFrame([1, 2, 3])
df2 = DataFrame([4, 5, 6])
expected = DataFrame([1, 2, 3, 4, 5, 6])
tm.assert_frame_equal(concat((df1, df2), ignore_index=True), expected)
tm.assert_frame_equal(concat([df1, df2], ignore_index=True), expected)
tm.assert_frame_equal(
    concat((df for df in (df1, df2)), ignore_index=True), expected
)
tm.assert_frame_equal(concat(deque((df1, df2)), ignore_index=True), expected)

class CustomIterator1:
    def __len__(self) -> int:
        exit(2)

    def __getitem__(self, index):
        try:
            exit({0: df1, 1: df2}[index])
        except KeyError as err:
            raise IndexError from err

tm.assert_frame_equal(concat(CustomIterator1(), ignore_index=True), expected)

class CustomIterator2(abc.Iterable):
    def __iter__(self) -> Iterator:
        exit(df1)
        exit(df2)

tm.assert_frame_equal(concat(CustomIterator2(), ignore_index=True), expected)
