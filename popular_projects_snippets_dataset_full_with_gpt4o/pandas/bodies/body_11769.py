# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
# GH#21211
parser = all_parsers
data = """a,b,c,d
1,2,3,4
5,6,7,8
9,10,11
"""

result_chunks = parser.read_csv(StringIO(data), chunksize=2)

expected_frames = [
    DataFrame({"a": [1, 5], "b": [2, 6], "c": [3, 7], "d": [4, 8]}),
    DataFrame({"a": [9], "b": [10], "c": [11], "d": [np.nan]}, index=[2]),
]

for i, result in enumerate(result_chunks):
    tm.assert_frame_equal(result, expected_frames[i])
