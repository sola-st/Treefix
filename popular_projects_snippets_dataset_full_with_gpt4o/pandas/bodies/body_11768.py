# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
# GH#21211
parser = all_parsers
data = """1,2,3,4
5,6,7,8
9,10,11
"""

result_chunks = parser.read_csv(
    StringIO(data),
    names=["a", "b"],
    chunksize=2,
    usecols=[0, 1],
    header=None,
)

expected_frames = [
    DataFrame({"a": [1, 5], "b": [2, 6]}),
    DataFrame({"a": [9], "b": [10]}, index=[2]),
]

for i, result in enumerate(result_chunks):
    tm.assert_frame_equal(result, expected_frames[i])
